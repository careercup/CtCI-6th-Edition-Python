# O(N)
import unittest


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    string = ""
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return string.join(char_list)


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(" ", "%20")


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [
        ("much ado about nothing      ", "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", "Mr%20John%20Smith"),
    ]
    testable_functions = [urlify_algo, urlify_pythonic]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for test_string, expected in self.test_cases:
                stripped_length = len(test_string.rstrip(" "))
                actual = urlify(test_string, stripped_length)
                assert actual == expected


if __name__ == "__main__":
    unittest.main()
