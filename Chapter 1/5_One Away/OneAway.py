# O(N)
import unittest


def one_away(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def one_away__alternative(s1, s2):
    """An alternative to the `one_away` above.
    Based on the CPP approach in https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter%201/5_One%20Away/OneAway.py

    Iterate over both strings checking for equality.

    When a first mismatch occurs:
    * if strings are of equal lengths, assume replacement
    * if one is shorter, delay its pointer
    Fail on second mismatch.

    """
    l1 = len(s1)
    l2 = len(s2)

    if abs(l1 - l2) > 1:
        return False

    if l1 < l2:
        shorter, longer = s1, s2
    else:
        # might be a misnomer if they're equal length, it doesn't matter
        # as long as 'longer' isn't shorter than 'shorter'
        shorter, longer = s2, s1

    equal_length = l1 == l2
    mismatch_occurred = False
    i, j = 0, 0
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            if mismatch_occurred:
                # second mismatch, second edit occured, fail
                return False
            mismatch_occurred = True
            if equal_length:
                # "replace" case, move both pointers (j moved later on)
                i += 1
        else:
            # move both pointers (j moved later on) but not for the first mismatch
            i += 1
        # always move long string pointer
        j += 1
    return True


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
            actual = one_away__alternative(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
