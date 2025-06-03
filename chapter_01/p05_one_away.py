# O(N)
import time
import unittest
from typing import Callable


def are_one_edit_different(s1: str, s2: str) -> bool:
    """
    Checks if two strings are at most one edit (insert, remove, or replace) away from each other.
    Time complexity: O(N), where N is the length of the shorter string.
    Space complexity: O(1).
    """
    len_s1: int = len(s1)
    len_s2: int = len(s2)

    if len_s1 == len_s2:
        return one_edit_replace(s1, s2)
    if len_s1 + 1 == len_s2:
        return one_edit_insert(s1, s2)  # s1 is shorter
    if len_s1 - 1 == len_s2:
        return one_edit_insert(s2, s1)  # s2 is shorter, so effectively a delete from s1
    return False


def one_edit_replace(s1: str, s2: str) -> bool:
    """Helper for are_one_edit_different: checks for one replacement."""
    edited: bool = False
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1_shorter: str, s2_longer: str) -> bool:
    """Helper for are_one_edit_different: checks for one insertion.
    s1_shorter is the shorter string, s2_longer is the longer string.
    """
    edited: bool = False
    idx_shorter: int = 0
    idx_longer: int = 0
    while idx_shorter < len(s1_shorter) and idx_longer < len(s2_longer):
        if s1_shorter[idx_shorter] != s2_longer[idx_longer]:
            if edited:
                return False
            edited = True
            idx_longer += 1  # Increment only longer string's index (simulating insert)
        else:
            idx_shorter += 1
            idx_longer += 1
    return True


class Test(unittest.TestCase):
    """Tests for the one-away string edit distance functionality."""
    test_cases: list[tuple[str, str, bool]] = [
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
        # permutation with insert shouldn't match
        ("ale", "elas", False),
        # Unicode characters
        ("pale", "pæle", True),  # Replace 'a' with 'æ'
        ("résumé", "resume", True), # Replace 'é' with 'e'
        ("résumé", "resum", True),  # Remove 'é'
        ("resume", "résumé", True), # Insert 'é'
        ("Straße", "Strasse", False), # 'ß' to 'ss' is two edits (remove ß, insert s, insert s) or one complex substitution
                                     # if lengths are same, e.g. "Straze" vs "Strasse" would be one edit.
        ("Straβe", "Strasse", True), # Assuming β (Greek beta) is different from ß (German eszett) and s. Replace β with s.
                                     # This test depends on exact character codes.
                                     # Let's use more distinct examples if there's ambiguity.
        ("你好", "你好", True), # No change, non-ASCII
        ("你好", "你好a", True), # Insert 'a'
        ("你好a", "你好", True), # Remove 'a'
        ("你好", "我好", True), # Replace '你' with '我'
        ("你好", "我不好", False), # More than one edit
    ]

    testable_functions: list[Callable[[str, str], bool]] = [are_one_edit_different]

    def test_one_away(self) -> None:
        """
        Tests the are_one_edit_different function with various cases.
        Includes a simple performance measurement over multiple runs.
        """
        for one_away_func in self.testable_functions:
            start_time: float = time.perf_counter()
            num_test_iterations = 100 # Number of times to run all test_cases for benchmark
            for _ in range(num_test_iterations):
                for text_a, text_b, expected_result in self.test_cases:
                    actual_result = one_away_func(text_a, text_b)
                    assert actual_result == expected_result, (
                        f"{one_away_func.__name__}('{text_a}', '{text_b}') was {actual_result} "
                        f"but expected {expected_result}"
                    )
            duration: float = time.perf_counter() - start_time
            print(
                f"{one_away_func.__name__} performance: {duration * 1000:.1f}ms "
                f"for {num_test_iterations} iterations of all test cases."
            )


if __name__ == "__main__":
    unittest.main()
