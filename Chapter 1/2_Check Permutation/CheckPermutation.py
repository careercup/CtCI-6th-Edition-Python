# O(N)
import unittest

def check_permutation(string):
    s1, s2 = sorted(string[0]), sorted(string[1])
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)-1):
        if s1[i] != s2[i]:
            return False
    return True

class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
