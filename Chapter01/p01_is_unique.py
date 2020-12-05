# O(N)
import unittest


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
    ]

    def test_is_unique_chars(self):
        for text, expected in self.test_cases:
            assert is_unique_chars_algorithmic(text) == expected


if __name__ == "__main__":
    unittest.main()
