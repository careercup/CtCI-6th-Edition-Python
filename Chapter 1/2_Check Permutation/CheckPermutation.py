def check_permutation(string_array):
    # function checks if a string is permutation of another
    if len(string_array[0]) == len(string_array[1]):
        return sorted(string_array[0]) == sorted(string_array[1])
    return False


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
