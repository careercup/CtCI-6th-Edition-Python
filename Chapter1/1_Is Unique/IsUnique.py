# O(N)
import unittest


def is_unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class IsUniqueTest(unittest.TestCase):

    def test_true_check(self):
        dataT = [('abcd'), ('s4fad'), ('')]
        for test_string in dataT:
            self.assertTrue(is_unique(test_string))

    def test_false_check(self):
        dataF = [('23ds2'), ('hb 627jh=j ()')]
        for test_string in dataF:
            self.assertFalse(is_unique(test_string))

if __name__ == "__main__":
    unittest.main()
