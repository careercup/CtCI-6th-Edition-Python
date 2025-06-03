# O(NxN)
import unittest
from copy import deepcopy
from typing import Callable

# Type alias for a matrix
Matrix = list[list[int]]


def rotate_matrix(matrix: Matrix) -> Matrix:
    """
    Rotates an N x N matrix 90 degrees clockwise in-place.
    Time complexity: O(N*N), as each element is touched a constant number of times.
    Space complexity: O(1), as the rotation is done in-place.
    """
    n: int = len(matrix)
    if n == 0:
        return [] # Standard return for empty matrix

    # Validate if the matrix is square (N x N)
    if not all(isinstance(row, list) and len(row) == n for row in matrix):
        # Or raise ValueError("Matrix must be N x N and non-jagged.")
        return matrix # Return original matrix if not square or jagged

    for layer in range(n // 2):
        first: int = layer
        last: int = n - layer - 1
        for i in range(first, last):
            offset: int = i - first
            # save top
            top: int = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix


def rotate_matrix_pythonic(matrix: Matrix) -> Matrix:
    """
    Rotates an N x N matrix 90 degrees clockwise by creating a new matrix.
    Time complexity: O(N*N) to iterate through all elements.
    Space complexity: O(N*N) for the new result matrix.
    """
    n: int = len(matrix)
    if n == 0:
        return [] # Standard return for empty matrix

    # Validate if the matrix is square (N x N)
    if not all(isinstance(row, list) and len(row) == n for row in matrix):
        # Or raise ValueError("Matrix must be N x N and non-jagged.")
        return matrix # Return original matrix if not square or jagged

    # Initialize the result matrix with zeros
    # Using _ for the loop variable as its value is not used inside the list comprehension
    result: Matrix = [[0 for _col in range(n)] for _row in range(n)]

    for r_idx in range(n):  # r_idx for row index in original matrix
        for c_idx in range(n):  # c_idx for column index in original matrix
            result[c_idx][n - 1 - r_idx] = matrix[r_idx][c_idx]

    return result


def rotate_matrix_pythonic_alternate(matrix):
    """rotates a matrix 90 degrees clockwise"""
    return [list(reversed(row)) for row in zip(*matrix)]


class Test(unittest.TestCase):
    """Tests for matrix rotation functions."""

    # Test cases: (original_matrix, expected_rotated_matrix)
    test_cases: list[tuple[Matrix, Matrix]] = [ # Changed List to list
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
        ([], []),  # Test with an empty matrix
        ([[1]], [[1]]),  # Test with a single element matrix
    ]


    def test_rotate_matrix(self) -> None:
        """
        Tests both matrix rotation implementations against predefined valid square matrix test cases.
        Ensures that in-place modifications do not affect subsequent tests by using deepcopy.
        """
        for rotate_func in self.testable_functions:
            for original_matrix, expected_matrix in self.test_cases:
                # Use deepcopy for the matrix to be rotated, as one function is in-place
                matrix_to_rotate = deepcopy(original_matrix)
                actual_matrix = rotate_func(matrix_to_rotate)
                assert actual_matrix == expected_matrix, (
                    f"{rotate_func.__name__} with input {original_matrix} produced "
                    f"{actual_matrix}, but expected {expected_matrix}"
                )

    def test_rotate_matrix_invalid_input(self) -> None:
        """
        Tests matrix rotation functions with invalid inputs (e.g., non-square, jagged).
        These are expected to return the original matrix due to validation checks.
        """
        invalid_matrices = [
            [[]],  # List containing one empty list
            [[1, 2], [3]], # Jagged matrix
            [[1, 2, 3], [4, 5]], # Jagged matrix
            # The following are not List[List[int]] so would be type errors ideally,
            # but current validation returns them as is.
            # If type checking were strict at runtime and raised errors, tests would use assertRaises.
            [1, 2, 3], # Not a list of lists
            [[1, 2], "string", [3, 4]], # A row is not a list
            None, # Test with None input
        ]

        for rotate_func in self.testable_functions:
            for invalid_matrix_input in invalid_matrices:
                # For None input, we expect a TypeError from len() before our validation.
                # This test structure is primarily for inputs that make it to our validation logic.
                if invalid_matrix_input is None:
                    with self.assertRaises(TypeError):
                        rotate_func(invalid_matrix_input)
                    continue

                # deepcopy might fail for mixed types like [[1,2], "string"],
                # so we pass the original if deepcopy fails for such heterogeneous structures.
                try:
                    matrix_to_test = deepcopy(invalid_matrix_input)
                    expected_output = invalid_matrix_input # Expect original back
                except TypeError: # deepcopy failed (e.g. for [1,2,3] or mixed types)
                    matrix_to_test = invalid_matrix_input
                    expected_output = invalid_matrix_input

                actual_output = rotate_func(matrix_to_test)
                assert actual_output == expected_output, (
                    f"{rotate_func.__name__} with invalid input {invalid_matrix_input} "
                    f"produced {actual_output}, but expected {expected_output}"
                )


if __name__ == "__main__":
    unittest.main()
