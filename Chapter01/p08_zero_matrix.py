# O(MxN)
import unittest
from copy import deepcopy


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []
    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            matrix[idx] = [0] * len(matrix[0])
    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix, zero_matrix_pythonic]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
