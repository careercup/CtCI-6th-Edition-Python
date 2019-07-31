# O(N)
import unittest


def palindrome_permutation(string):
    # No lowercase, ignore special characters
    string = [char for char in string.lower() if ord(char) in range(97, 123)]
    # to be a palindrome, the count of each letter has to be even, save for one letter that can be odd.
    my_dict = {char: string.count(char) for char in set(string)}
    odd_list = [char for char, count in my_dict.items() if count % 2 != 0]
    return len(odd_list) <= 1


def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
