import time
import unittest
from collections import defaultdict
from typing import Callable


def is_unique_chars_algorithmic(string: str) -> bool:
    """
    Determines if a string has all unique characters using a boolean array.
    Assumes the character set is ASCII (128 characters).
    Time complexity: O(N), where N is the length of the string (at most 128).
    Space complexity: O(1) (boolean array size is fixed at 128).
    """
    if len(string) > 128: # Based on ASCII assumption
        return False

    char_set: list[bool] = [False] * 128 # Boolean array to track characters
    for char_code in map(ord, string):
        if char_code > 127:
            # Character out of assumed ASCII range
            return False # Or raise ValueError("Non-ASCII character found")
        if char_set[char_code]:
            # Char already found in string
            return False
        char_set[char_code] = True

    return True


def is_unique_chars_pythonic(string: str) -> bool:
    """
    Determines if a string has all unique characters using Python's set properties.
    Time complexity: O(N) on average, where N is the length of the string.
    Space complexity: O(N) in the worst case for the set.
    """
    return len(set(string)) == len(string)


def is_unique_bit_vector(string: str) -> bool:
    """
    Determines if a string has all unique characters using a bit vector.
    Assumes the character set is ASCII (128 characters, fitting within integer bits if extended).
    This implementation assumes characters 'a' through 'z' or a similar limited range
    if not strictly ASCII values that might exceed typical integer bit sizes for a direct bit vector.
    For full ASCII (0-127), this approach is fine.
    Time complexity: O(N).
    Space complexity: O(1).
    """
    # Assuming character set is ASCII (128 characters) for this specific check
    if len(string) > 128: # Optimization for this assumption
        return False

    checker: int = 0
    for char_code in map(ord, string):
        if char_code > 127:
            # Character out of assumed ASCII range for this bit vector approach
            return False # Or raise ValueError("Non-ASCII character found")
        if (checker & (1 << char_code)) > 0:
            return False
        checker |= (1 << char_code)
    return True


def is_unique_chars_using_dictionary(string: str) -> bool:
    """
    Determines if a string has all unique characters using a dictionary (hash map).
    Time complexity: O(N) on average, where N is the length of the string.
    Space complexity: O(K), where K is the number of unique characters (at most N).
    """
    character_counts: dict[str, bool] = {} # Stores seen characters
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = True # Value can be True, or a count, doesn't matter
    return True


def is_unique_chars_sorting(string: str) -> bool:
    """
    Determines if a string has all unique characters by sorting it first.
    Time complexity: O(N log N) due to sorting.
    Space complexity: O(N) or O(log N) depending on sort implementation (Python's Timsort is O(N)).
    """
    if not string:
        return True
    sorted_string = sorted(string)
    last_character = sorted_string[0]
    for i in range(1, len(sorted_string)):
        if sorted_string[i] == last_character:
            return False
        last_character = sorted_string[i]
    return True


# Sorting without extra variable. TC: O(NlogN) SC: O(1) Con: Modifies input string
def is_unique_chars_sort(string: str) -> bool:
    string = sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


class Test(unittest.TestCase):
    """Tests for the various is_unique_chars implementations."""

    test_cases: list[tuple[str, bool]] = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions: list[Callable[[str], bool]] = [
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
        is_unique_chars_using_dictionary,
        is_unique_chars_using_set,
        is_unique_chars_sorting,
        is_unique_chars_sort,
    ]

    def test_is_unique_chars(self) -> None:
        """
        Runs all is_unique_chars implementations against general test cases.
        Also performs a mini-benchmark and prints the runtimes.
        """
        num_runs: int = 1000
        # Using defaultdict to store sum of runtimes for each function
        function_runtimes: defaultdict[str, float] = defaultdict(float)

        for _ in range(num_runs):
            for text, expected_result in self.test_cases:
                for is_unique_func in self.test_functions:
                    start_time: float = time.perf_counter()
                    actual_result = is_unique_func(text)
                    assert actual_result == expected_result, (
                        f"{is_unique_func.__name__}('{text}') returned {actual_result}, "
                        f"expected {expected_result}"
                    )
                    function_runtimes[is_unique_func.__name__] += (
                        time.perf_counter() - start_time
                    ) * 1000 # Convert to milliseconds

        print(f"\nBenchmark Results ({num_runs} runs per function):")
        for function_name, total_runtime in function_runtimes.items():
            # Calculate average runtime if needed, or print total as is
            print(f"{function_name}: {total_runtime:.1f}ms (total)")

    def test_non_ascii_handling(self) -> None:
        """
        Tests how different implementations handle non-ASCII characters.
        - _algorithmic and _bit_vector should return False due to ASCII constraint.
        - Other methods should handle them as regular characters.
        """
        non_ascii_test_cases = [
            # (input_string, expected_for_ascii_limited_funcs, expected_for_unicode_funcs)
            ("abcä", False, True), # 'ä' is non-ASCII
            ("ü", False, True),    # 'ü' is non-ASCII
            ("äöü", False, True),  # All non-ASCII, but unique among themselves
            ("äbä", False, False), # Non-unique non-ASCII for Unicode funcs
            ("€uro", False, True), # Euro sign
        ]

        for text, expected_ascii, expected_unicode in non_ascii_test_cases:
            for func in self.test_functions:
                is_ascii_limited = func.__name__ in (
                    "is_unique_chars_algorithmic",
                    "is_unique_bit_vector",
                )
                expected = expected_ascii if is_ascii_limited else expected_unicode
                actual = func(text)
                assert actual == expected, (
                    f"{func.__name__}('{text}') returned {actual}, expected {expected}"
                )


if __name__ == "__main__":
    unittest.main()
