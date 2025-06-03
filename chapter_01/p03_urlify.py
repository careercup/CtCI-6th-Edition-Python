# O(N)
import unittest
from typing import Callable


def urlify_algo(s: str, length: int) -> str:
    """
    Replaces spaces in a string with '%20'.
    Operates on a list copy of the string, assuming the original string (represented by `s`)
    has sufficient trailing space to accommodate the additional characters if it were
    a mutable character array. The `length` parameter indicates the "true" length
    of the content in `s`.

    Time complexity: O(N), where N is the length of the string `s`.
    Space complexity: O(N) for `char_list`.
    """
    if length < 0:
        # Or raise ValueError("length cannot be negative")
        return "Error: length cannot be negative" # Placeholder for error handling
    if length > len(s):
        # Or raise ValueError("length cannot exceed string length")
        return "Error: length exceeds string length" # Placeholder for error handling

    if length == 0:
        return ""

    # Convert string to list to simulate in-place modification of a char array
    # The problem often implies 's' is a pre-allocated buffer. Here, list(s) copies it.
    # The original problem in CTCI assumes the list/array is already large enough.
    char_list: list[str] = list(s)
    # new_index points to the position where the next character from the original string
    # (or '%20') should be placed, moving from the end of the buffer towards the start.
    # For this to work as a C-style in-place modification, len(s) (the buffer size)
    # must be >= length + 2 * (number of spaces in s[:length]).
    # Python lists handle resizing with slice assignment, which might mask true C-style buffer overflows
    # but can lead to unexpected behavior if not careful with indices.
    # The current implementation relies on returning `"".join(char_list[new_index:])`,
    # so `new_index` must end up at the actual start of the urlified content.

    # Calculate required final length to check if original s buffer was notionally sufficient
    num_spaces = 0
    for i in range(length):
        if s[i] == ' ':
            num_spaces += 1

    # new_index will be the "write pointer" for the end of the conceptual final string.
    # It should start at where the end of the urlified string would be if s was just long enough.
    # However, the problem implies s is the buffer, potentially oversized.
    # So, new_index starts at the end of the provided buffer s.
    new_index: int = len(char_list)


    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = list("%20")
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    # The URLified part of the string is at the end of char_list, from new_index onwards.
    return "".join(char_list[new_index:])


def urlify_pythonic(text: str, length: int) -> str:
    """
    Replaces spaces in a string with '%20' using Python's string methods.
    The `length` parameter indicates the "true" length of the content in `text`.

    Time complexity: O(N), where N is `length`. Slicing is O(length), replace is O(length).
    Space complexity: O(N) for the new string.
    """
    if length < 0:
        # Or raise ValueError("length cannot be negative")
        return "Error: length cannot be negative" # Placeholder for error handling
    # text[:length] handles length > len(text) gracefully (slices to end).
    # Process only the relevant part of the string (up to `length`) and replace spaces.

    # convert back to string
    return "".join(char_list[new_index:])



    return text[:length].replace(" ", "%20")


class Test(unittest.TestCase):
    """Tests for URLify functions."""


    # Test cases: (input_string_with_buffer, true_length, expected_urlified_string)
    test_cases: list[tuple[str, int, str]] = [
        ("much ado about nothing      ", 24, "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("  leading spaces  ", 18, "%20%20leading%20spaces"),
        ("no_spaces", 9, "no_spaces"),
        ("trailing space   ", 15, "trailing%20space"), # "trailing space " has length 15
        ("singlechar", 10, "singlechar"),
        (" space at end    ", 13, "space%20at%20end"), # " space at end" has length 13
        ("  ", 2, "%20%20"), # Only spaces
        ("", 0, ""), # Empty string
    ]
    testable_functions: list[Callable[[str, int], str]] = [urlify_algo, urlify_pythonic]

    def test_urlify(self) -> None:
        """Runs all URLify implementations against valid test cases."""
        for urlify_func in self.testable_functions:
            for test_string_with_buffer, true_length, expected_output in self.test_cases:
                actual_output = urlify_func(test_string_with_buffer, true_length)
                assert actual_output == expected_output, (
                    f"{urlify_func.__name__}('{test_string_with_buffer}', {true_length}) "
                    f"produced '{actual_output}', but expected '{expected_output}'"
                )

    def test_urlify_invalid_length(self) -> None:
        """Tests URLify functions with invalid length parameters."""
        invalid_length_cases = [
            # (function_to_test, input_string, invalid_length, expected_behavior)
            # For urlify_algo, specific error strings are returned
            (urlify_algo, "test string", -1, "Error: length cannot be negative"),
            (urlify_algo, "test", 5, "Error: length exceeds string length"), # len("test") is 4
            # For urlify_pythonic
            (urlify_pythonic, "test string", -1, "Error: length cannot be negative"),
            (urlify_pythonic, "test", 5, "test"), # Slices gracefully, then replaces spaces
            (urlify_pythonic, "test space", 11, "test%20space"), # len is 10, length 11 slices to end
        ]

        for func, s, length, expected in invalid_length_cases:
            actual = func(s, length)
            assert actual == expected, (
                f"{func.__name__}('{s}', {length}) produced '{actual}', expected '{expected}'"
            )



if __name__ == "__main__":
    unittest.main()
