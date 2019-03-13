# O(N)
import unittest


def urlify(string, length):
    """function replaces single spaces with %20 and removes trailing spaces"""
    index = len(string)
    str_list = list(string)

    for i in reversed(range(length)):
        if str_list[i] == " ":
            # Replace spaces
            str_list[index - 3:index] = "%20"
            index -= 3
        else:
            # Move characters
            str_list[index - 1] = str_list[i]
            index -= 1

    return "".join(str_list)


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
    ]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
