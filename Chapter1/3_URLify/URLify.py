# O(N)
import unittest

#you need 1 extra pass to get the right starting point, since the given string may contain more 
#spaces than needed

def add_space(n_space):
    return n_space+1

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    #first pass to count the number of space in the true string
    
    n_space = 0
    for i in range(length): 
        if string[i] == ' ':
            n_space+=1
    
    
    new_index = length + 2*n_space

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1
   
    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing           '), 22,
         list('much%20ado%20about%20nothing     ')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    """
    data = [
        (list('much ado about nothing           '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    urlify(data[0][0],data[0][1])"""
