# O(N)
import unittest


def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)
    char_list = list(string)

    for i in reversed(range(length)):
        if char_list[i] == ' ':
            # Replace spaces
            char_list[new_index - 3:new_index] = ['%','2','0']
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return "".join(char_list)


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
