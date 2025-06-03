# O(N) - where N is the length of the strings. The check `s2 in s1 * 2` can take O(N*N) in naive implementations,
# but Python's `in` operator for strings is highly optimized (e.g., using Boyer-Moore or similar),
# making it closer to O(N) on average for creating s1*2 and then the lookup.
import unittest

# List, Tuple removed from typing import


def string_rotation(s1: str, s2: str) -> bool:
    """
    Checks if s2 is a rotation of s1.
    Example: "waterbottle" is a rotation of "erbottlewat".

    The core idea is that if s2 is a rotation of s1, then s2 must be a
    substring of s1 concatenated with itself (s1s1).
    Assumes an isSubstring check (Python's `in` operator for strings).

    Time complexity: O(N) on average for creating s1+s1 and the substring check.
                     Python's `in` operator is highly optimized.
                     (Worst case for naive substring can be O(N*M), but not typical for Python).
    Space complexity: O(N) for the concatenated string s1+s1.
    """
    if (
        len(s1) == len(s2) and len(s1) > 0
    ):  # Ensure strings are non-empty and have same length
        return s2 in (s1 + s1)
    # If lengths are different or strings are empty, they can't be rotations.
    # Some definitions might consider two empty strings as rotations of each other (True).
    # Here, following common interpretation, empty strings are not rotations.
    return False


class Test(unittest.TestCase):
    """Tests for the string_rotation function."""

    test_cases: list[tuple[str, str, bool]] = [  # Changed to built-in list and tuple
        ("waterbottle", "erbottlewat", True),
        ("hello", "lohel", True),
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),  # Not a rotation
        ("foo", "bar", False),
        ("foo", "foofoo", False),  # s2 is longer
        ("aa", "a", False),  # s2 is shorter
        ("topcoder", "coderbot", False),  # Same letters, not rotation
        ("", "", False),  # Empty strings
        ("a", "a", True),  # Single character strings, considered rotation
        ("ab", "ba", True),  # Simple rotation
        ("abc", "abc", True),  # Rotation of itself (0 shift)
        # Unicode tests
        ("你好世界", "世界你好", True),
        ("résumé", "suméré", True), # "suméré" is a rotation of "résumé"
        ("你好", "好你", True),
        ("你好", "你不好", False), # Different content and length
        ("€uro", "ro€u", True),
    ]

    def test_string_rotation(self) -> None:
        """
        Tests the string_rotation function against various predefined test cases.
        """
        for s1_test, s2_test, expected_result in self.test_cases:
            actual_result = string_rotation(s1_test, s2_test)
            assert actual_result == expected_result, (
                f"string_rotation('{s1_test}', '{s2_test}') was {actual_result}, "
                f"but expected {expected_result}"
            )


if __name__ == "__main__":
    unittest.main()
