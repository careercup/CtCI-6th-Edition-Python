# O(N)
import unittest


def string_compression(INPUT):
    strings = [] #ordered list of INPUT divided into identical sequences
    char = INPUT[0]
    for i in range(1, len(INPUT)+1): #iterate through length of INPUT
        if i == len(INPUT): #if last sequence in string
            strings = strings + [char]
        elif INPUT[i] == INPUT[i-1]: #if current character is same as previous
            char = char + INPUT[i]
        else:
            strings = strings + [char]
            char = INPUT[i]
    result = ''.join([x[0]+str(len(x)) for x in strings]) #first item of substring + len of substring, joined into a string
    if len(result) < len(INPUT):
        return result
    return INPUT


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
