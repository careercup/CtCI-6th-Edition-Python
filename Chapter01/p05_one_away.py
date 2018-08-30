# O(N)
import time
import unittest


def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
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


def are_one_edit_different_sets(a, b):
    """Implementation using sets"""
    # Case 1 : The two strings have the same length.
    if len(a) == len(b):

        # Case 1.1 : No edits away, i.e the strings are identical.
        if a == b:
            return True

        # Case 1.2 : The string is just 1 edit away,
        #            which in this case would just be
        #            one character replaced.
        if len(set(a) & set(b)) == len(a) - 1:
            return True

    # Case 2 : The two strings are of different lengths
    elif abs(len(a) - len(b)) == 1:

        smaller_strlen = min(len(a), len(b))

        # Case 2.1 : The only scenario where this should return True
        #            is when the strings are 1 removal or insertion
        #            away. So, the length of the intersection of the
        #            2 strings in sets should be equal to the length
        #            of the smaller string.
        if len(set(a) & set(b)) == smaller_strlen:
            return True

    # Case 3 : The two strings are not 1 or 0 edits away
    return False


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    testable_functions = [are_one_edit_different, are_one_edit_different_sets]

    def test_one_away(self):

        for are_one_edit_different in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert are_one_edit_different(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{are_one_edit_different.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
