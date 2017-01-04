# O(N)
import unittest


def one_away(str1, str2):
    d1, d2 = {}, {}
    for i in str1.lower():
        if i in d1.keys():
            d1[i] += 1
        else:
            d1[i] = 1
    for i in str2.lower():
        if i in d2.keys():
            d2[i] += 1
        else:
            d2[i] = 1
    if len(set(d1.items()) - set(d2.items())) in [0, 1] and len(set(d2.items()) - set(d1.items())) in [0, 1]:
        return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
