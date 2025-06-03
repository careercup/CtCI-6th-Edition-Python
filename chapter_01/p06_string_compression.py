import time
import unittest
from typing import Callable
import itertools # Added for groupby


def compress_string(s: str) -> str:
    """
    Compresses a string by counting consecutive repeating characters.
    Example: "aabcccccaaa" -> "a2b1c5a3".
    If the "compressed" string is not smaller than the original, the original is returned.
    Handles empty strings.

    Time complexity: O(N), as itertools.groupby iterates through the string once,
                     and string joining also takes about O(N).
    Space complexity: O(N) in the worst case (e.g., "abcde" becomes "a1b1c1d1e1").
    """
    if not s:
        return ""

    # Use itertools.groupby to group consecutive identical characters
    # For each character and its group, form the char + count string part
    compressed_parts = [
        char + str(len(list(group))) for char, group in itertools.groupby(s)
    ]
    compressed_s = "".join(compressed_parts)

    # Return the shorter of the original string or the compressed string
    return s if len(s) <= len(compressed_s) else compressed_s


class Test(unittest.TestCase):
    """Tests for the string_compression function."""

    test_cases: list[tuple[str, str]] = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),  # No compression beneficial
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
        ("AAABCCCDDDD", "A3B1C3D4"),  # Test with uppercase
        ("aaAAaa", "a2A2a2"),  # Test with mixed case as distinct chars
        # Unicode character tests
        ("äääbbbccc", "ä3b3c3"),
        ("üüüüü", "ü5"),
        ("你好你好", "你1好1你1好1"), # Consecutive grouping
        ("你你你好好好", "你3好3"),
        ("abcäöü", "abcäöü"), # No compression for unique Unicode chars
        ("aaabbbäää", "a3b3ä3"),
    ]
    testable_functions: list[Callable[[str], str]] = [
        compress_string,
    ]

    def test_string_compression(self) -> None:
        """
        Tests the compress_string function with various cases.
        Includes a simple performance measurement.
        """
        for compress_func in self.testable_functions:
            start_time: float = time.perf_counter()
            num_test_iterations = 1000  # Number of times to run all test_cases
            for _ in range(num_test_iterations):
                for test_string, expected_result in self.test_cases:
                    actual_result = compress_func(test_string)
                    assert actual_result == expected_result, (
                        f"{compress_func.__name__}('{test_string}') produced {actual_result}, "
                        f"expected {expected_result}"
                    )
            duration: float = time.perf_counter() - start_time
            print(
                f"{compress_func.__name__} performance: {duration * 1000:.1f}ms "
                f"for {num_test_iterations} iterations of all test cases."
            )


if __name__ == "__main__":
    unittest.main()
