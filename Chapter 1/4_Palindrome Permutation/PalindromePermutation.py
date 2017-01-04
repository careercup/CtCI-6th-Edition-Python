# O(N)
import unittest


def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    phrase = phrase.replace(" ", "").lower()
    dic = {}
    for i in phrase:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    if len(phrase) % 2 == 0:
        if all(value % 2 == 0 for value in set(dic.values())):
            return True
    else:
        print "touches odd"
        vals = dic.values()
        if vals.count(1) == 1:
            vals.remove(1)
            if all(value % 2 == 0 for value in set(vals)):
                return True
    return False



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
