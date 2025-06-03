# O(N)
import string
import unittest
from collections import Counter
from typing import Callable


def is_palindrome_permutation(phrase: str) -> bool:
    """
    Checks if a string can be rearranged to form a palindrome.
    This method uses a frequency table (list) for character counts.
    It is case-insensitive and ignores non-alphabetic characters.

    Time complexity: O(N), where N is the length of the phrase.
    Space complexity: O(1) (table size is fixed for the alphabet).
    """
    # Frequency table for 'a' through 'z', ignoring case.
    table: list[int] = [0] * (ord("z") - ord("a") + 1)
    odd_frequency_count: int = 0
    for char_in_phrase in phrase:
        char_idx = char_number(char_in_phrase)
        if char_idx != -1:
            table[char_idx] += 1
            if table[char_idx] % 2 == 1:
                odd_frequency_count += 1
            else:
                odd_frequency_count -= 1
    # A string can be a permutation of a palindrome if at most one character
    # has an odd frequency.
    return odd_frequency_count <= 1


def char_number(char_code: str) -> int:
    """
    Converts an alphabetic character to a 0-25 index (case-insensitive).
    Returns -1 if the character is not alphabetic.
    'a'/'A' -> 0, 'b'/'B' -> 1, ..., 'z'/'Z' -> 25.
    """
    val: int = ord(char_code)
    a_lower: int = ord("a")
    z_lower: int = ord("z")
    a_upper: int = ord("A")
    z_upper: int = ord("Z")

    if a_lower <= val <= z_lower:
        return val - a_lower
    if a_upper <= val <= z_upper:
        return val - a_upper
    return -1 # Not an alphabetic character


def is_palindrome_permutation_pythonic(phrase: str) -> bool:
    """
    Checks if a string can be rearranged to form a palindrome using collections.Counter.
    This method is case-insensitive and considers only alphabetic characters.

    Time complexity: O(N), where N is the length of the phrase.
    Space complexity: O(K), where K is the number of unique alphabetic characters.
                     At most O(1) for a fixed alphabet size (e.g., 26 for English).
    """
    # Filter for alphabetic characters and convert to lowercase
    processed_chars = (char.lower() for char in phrase if char.isalpha())
    char_counts: Counter[str] = Counter(processed_chars)

    # Count how many characters have an odd frequency
    odd_frequency_count = sum(count % 2 for count in char_counts.values())


    return odd_frequency_count <= 1

def is_palindrome_bit_vector(phrase):
    """checks if a string is a permutation of a palindrome"""
    r = 0
    for c in clean_phrase(phrase):
        val = ord(c)
        mask = 1 << val
        if r & mask:
            r &= ~mask
        else:
            r |= mask
    return (r - 1) & r == 0


def is_palindrome_bit_vector2(phrase):
    """checks if a string is a permutation of a palindrome using XOR operation"""
    count_odd = 0
    for c in phrase:
        val = char_number(c)
        if val == -1:
            continue
        count_odd ^= 1 << val

    return count_odd & count_odd - 1 == 0


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(clean_phrase(phrase))
    return sum(val % 2 for val in counter.values()) <= 1



class Test(unittest.TestCase):
    """Tests for palindrome permutation functions."""
    test_cases: list[tuple[str, bool]] = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        (
            "azAZ",
            True,
        ),  # Original test, ensures case mapping works if non-alpha chars are ignored by char_number
        (" ", True),  # Test with only spaces
        ("  ", True),  # Test with only spaces
        ("aa bb cc", True),  # Test with spaces between valid chars
        ("Aa Bb Cc", True),  # Test with spaces and mixed case
        ("Taco cat", True),  # Common example
        ("Race car!", True),  # With punctuation
        # Test with non-Latin alphabetic characters
        ("АббА", True),  # Cyrillic, should be True for pythonic, True for table (as chars are ignored)
        ("키러키", True),  # Korean, should be True for pythonic, True for table (as chars are ignored)
        ("키키a", True),   # Mixed, pythonic True (a=1, 키=2), table True (a=1, 키 ignored)
    ]
    testable_functions: list[Callable[[str], bool]] = [
        is_palindrome_permutation,
        is_palindrome_permutation_pythonic,
    ]

    testable_functions = [
        is_palindrome_permutation,
        is_palindrome_bit_vector,
        is_palindrome_permutation_pythonic,
        is_palindrome_bit_vector2,
    ]


    def test_palindrome_permutation(self) -> None:
        """Runs all palindrome permutation check functions against defined test cases."""
        for pal_perm_func in self.testable_functions:
            for test_string, expected_result in self.test_cases:
                actual_result = pal_perm_func(test_string)
                assert actual_result == expected_result, (
                    f"{pal_perm_func.__name__}('{test_string}') produced {actual_result}, "
                    f"but expected {expected_result}"
                )


if __name__ == "__main__":
    unittest.main()
