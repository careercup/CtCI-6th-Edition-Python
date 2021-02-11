# O(N)
import unittest


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)


def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True


# O(NlogN)
def is_unique_chars_sorting(string: str) -> bool:
    if len(string) == 1 or len(string) == 0:
        return True
    sorted_string = sorted(string)
    last_character = sorted_string[0]
    for i in range(1, len(sorted_string)):
        if sorted_string[i] == last_character:
            return False
        last_character = sorted_string[i]
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
        is_unique_chars_using_dictionary,
        is_unique_chars_sorting,
    ]

    def test_is_unique_chars(self):
        for is_unique_chars in self.test_functions:
            for text, expected in self.test_cases:
                assert is_unique_chars(text) == expected


if __name__ == "__main__":
    unittest.main()
