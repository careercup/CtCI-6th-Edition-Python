# O(N)
import unittest
import numpy as np
import sys

def unique(string):
    # Assuming character set is ASCII (128 characters)
    #max_len = 128
    
    # Assuming all unicode set
    max_len = sys.maxunicode
    
    if len(string) > max_len:
        return False
        
        
    # np.ones or zeros is much faster than list comprehension 
    #especially for unicode set
    char_set = np.zeros((1, max_len), dtype=bool)
    #char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


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

if __name__ == "__main__":
    unittest.main()
