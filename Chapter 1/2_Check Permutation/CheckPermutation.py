# O(n)

def check_permutation(string_1, string_2):
    # function checks if a string is permutation of another
    if len(string_1) != len(string_2):
        return False

    string_dict = dict( [ (char, list(string_1).count(char)) for char in set(list(string_1)) ] )

    for char in string_2:
        if string_dict.get(char) == None or string_dict[char] < 0:
            return False
        else:
            string_dict[char] -= 1
    return True


class Test(unittest.TestCase):
    dataT = [('abcd', 'bacd'), ('3563476', '7334566'), ('wef34f', 'wffe34')]
    dataF = [('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f')]

    def test_cp(self):
        # true check
        for string_1, string_2 in self.dataT:
            actual = check_permutation(string_1, string_2)
            self.assertTrue(actual)
        # false check
        for string_1, string_2 in self.dataF:
            actual = check_permutation(string_1, string_2)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
