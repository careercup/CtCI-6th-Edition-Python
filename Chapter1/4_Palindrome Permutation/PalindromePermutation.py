# O(N)
import unittest

"""
def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1
"""
def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


#use dict and string.lower() can simplify the code a lot. and these are all build in function or primitive type. if you use python, you should accept this. 
def check_odd(string):
    ch_count = {}
    odd_count = 0
    
    string =  string.lower()
    for c in string:
        if c in ch_count:
            ch_count[c]+=1
        else:
            ch_count[c] = 1
   
    for k in ch_count:
        if ch_count[k]%2 != 0 :
            odd_count+=1
    return odd_count
        



def pal_perm(string):
    string = string.replace(' ','')
    length = len(string)
    
    odd_count = check_odd(string)

    re = False
    if odd_count <= 1:
        
       re = True
    return re




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
