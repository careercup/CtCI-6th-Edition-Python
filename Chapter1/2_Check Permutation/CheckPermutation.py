# O(max(s1, s2))
import unittest


def check_permutation(s1, s2):
    if(len(s1) != len(s2)):
        return False

    char_set = [0] * 256

    for letter in s1:
        ascii_val = ord(letter)
        char_set[ascii_val] += 1

    for letter in s2:
        ascii_val = ord(letter)
        char_set[ascii_val] -= 1

    for value in char_set:
        if(value != 0):
            return False

    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
