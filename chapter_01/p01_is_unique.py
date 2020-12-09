# O(N)
import unittest


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value. careful though
    # it won't work for a doubly nested array
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


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
    ]
    test_functions = [is_unique_chars_pythonic, is_unique_chars_algorithmic]

    def test_is_unique_chars(self):
        for is_unique_chars in self.test_functions:
            for text, expected in self.test_cases:
                assert is_unique_chars(text) == expected


if __name__ == "__main__":
    unittest.main()
