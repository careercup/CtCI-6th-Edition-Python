import time
import unittest
from collections import defaultdict

# git push test

# TC: O(n), n: length of s SC: O(1)
def is_unique_chars_algorithmic(s: str) -> bool:
    # assuming character set is ASCII(max 128 kind)
    if len(s) > 128:
        return False
    
    ascii_char = [False] * 128
    for char in s:
        val = ord(char)
        if ascii_char[val]:
            return False
        ascii_char[val] = True
    
    return True

# TC: O(n) SC: O(n) n: length of s
def is_unique_chars_pythonic(s: str) -> bool:
    return len(set(s)) == len(s)


def is_unique_bit_vector(s: str) -> bool:
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(s) > 128:
        return False

    checker = 0
    for c in s:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
        # is_unique_chars_using_dictionary,
        # is_unique_chars_using_set,
        # is_unique_chars_sorting,
        # is_unique_chars_sort,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
