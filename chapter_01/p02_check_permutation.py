# O(N)
import unittest
from collections import Counter
from typing import Callable


def check_permutation_by_sort(s1: str, s2: str) -> bool:
    """
    Checks if s2 is a permutation of s1 by sorting both strings.
    Time complexity: O(N log N) due to sorting, where N is the length of the strings.
    Space complexity: O(N) or O(log N) for sorting, depending on implementation.
    """
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    # After sorting, if they are permutations, they must be identical.
    for char1, char2 in zip(s1_sorted, s2_sorted):
        if char1 != char2:
            return False
    return True


def check_permutation_by_count(str1: str, str2: str) -> bool:
    """
    Checks if str2 is a permutation of str1 using character counts.
    Assumes an 8-bit character set (e.g., ASCII, up to 256 distinct characters).
    Time complexity: O(N), where N is the length of the strings.
    Space complexity: O(1) (fixed-size array for counts).
    """
    if len(str1) != len(str2):
        return False
    # Initialize counts for 256 possible characters (e.g., extended ASCII)
    char_counts: list[int] = [0] * 256

    for char_code in map(ord, str1):
        if char_code >= 256:
            # Character out of assumed 8-bit range
            return False # Or raise ValueError("Non-8bit character found")
        char_counts[char_code] += 1
    for char_code in map(ord, str2):
        if char_code >= 256:
            # Character out of assumed 8-bit range
            return False # Or raise ValueError("Non-8bit character found")
        if char_counts[char_code] == 0: # Found a char in str2 not in str1 or too many of it
            return False
        char_counts[char_code] -= 1
    # All counts should be zero if they are permutations
    return True


def check_permutation_pythonic(str1: str, str2: str) -> bool:
    """
    Checks if str2 is a permutation of str1 using collections.Counter.
    Time complexity: O(N), where N is the length of the strings.
    Space complexity: O(K), where K is the number of unique characters.
    """
    if len(str1) != len(str2):
        return False
    # Counter creates a hash map of character counts.
    # Two strings are permutations if their character counts are identical.
    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    """Tests for the different check_permutation implementations."""

    # Test cases: (string1, string2, expected_is_permutation)
    test_cases: tuple[tuple[str, str, bool], ...] = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions: list[Callable[[str, str], bool]] = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_check_permutation(self) -> None:
        """Runs all check_permutation functions against the defined general test cases."""
        for perm_function in self.testable_functions:
            for s1_test, s2_test, expected_result in self.test_cases:
                actual_result = perm_function(s1_test, s2_test)
                assert actual_result == expected_result, (
                    f"{perm_function.__name__}('{s1_test}', '{s2_test}') returned {actual_result}, "
                    f"expected {expected_result}"
                )

    def test_extended_character_handling(self) -> None:
        """
        Tests how different implementations handle characters beyond typical ASCII (0-255).
        - check_permutation_by_count should return False due to its 8-bit assumption.
        - Other methods should handle them as regular Unicode characters.
        """
        char_gt_255 = chr(256) # Example: 'Ā' Latin A with Macron

        # Test cases: (s1, s2, expected_for_8bit_limited_func, expected_for_unicode_funcs)
        extended_char_test_cases = [
            ("ab" + char_gt_255, char_gt_255 + "ba", False, True),
            (char_gt_255, char_gt_255, False, True),
            ("a" + char_gt_255 + "a", "aa" + char_gt_255, False, True),
            ("a" + char_gt_255, "b" + char_gt_255, False, False), # Not permutations
            # Test with a mix, one string having extended, other not (should be caught by length check first)
            # but if lengths match, this tests the char processing
            ("abc", "ab" + char_gt_255, False, False),
        ]

        # Add a case where one string has extended char and other doesn't, but lengths match due to other chars
        # This is implicitly covered if one function returns False due to char_code >= 256,
        # and the other function returns False because they are not permutations.
        # e.g. s1="Ā", s2="a". Lengths match.
        #   check_permutation_by_count("Ā", "a") -> False (due to Ā)
        #   check_permutation_by_sort("Ā", "a") -> False (sorted("Ā") != sorted("a"))
        #   check_permutation_pythonic("Ā", "a") -> False (Counter("Ā") != Counter("a"))
        # This existing structure should handle it.

        for s1, s2, expected_8bit, expected_unicode in extended_char_test_cases:
            for func in self.testable_functions:
                is_8bit_limited = func.__name__ == "check_permutation_by_count"

                expected = expected_8bit if is_8bit_limited else expected_unicode

                # For the case ("abc", "ab" + char_gt_255), expected_8bit is False.
                # If func is check_permutation_by_count, it will see char_gt_255 in s2 and return False. Correct.
                # If func is unicode-safe, it will also return False as they are not permutations. Correct.
                # So for this specific case, expected_8bit and expected_unicode are both False.

                actual = func(s1, s2)
                assert actual == expected, (
                    f"{func.__name__}('{s1}', '{s2}') returned {actual}, expected {expected}"
                )


if __name__ == "__main__":
    unittest.main()
