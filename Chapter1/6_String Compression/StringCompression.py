# O(N)
import unittest

def string_compression(string):

    # Optimized space complexity using just a string instead of an array
    output = ""
    char_counter = 1
    pointer = string[0]

    for index in range(1,len(string)):
        # Continue adding to the counter if the letter is the same
        if string[index] == pointer:
            char_counter +=1

        # Otherwise append to the string and reset the counter back to 1
        else:
            output += pointer
            output += str(char_counter)
            pointer = string[index]
            char_counter = 1

    return min(output + str(pointer) +str(char_counter), string, key = len)


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
