# O(N)
import unittest


def unique(string):
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

def unique_list_set(string):
    return len(list(string)) == len(set(list(string)))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

    def test_unique_list_set(self):
        # true check
        for test_string in self.dataT:
            actual = unique_list_set(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique_list_set(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
