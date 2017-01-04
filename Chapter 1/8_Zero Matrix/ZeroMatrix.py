# O(MxN)
import unittest


def zero_matrix(matrix):
    matrix = [['X' if x == 0 else x for x in row] for row in matrix]
    indices = []
    for idx, row in enumerate(matrix):
        if 'X' in row:
            indices =  indices + [i for i, j in enumerate(row) if j == 'X']
            matrix[idx] = [0]*len(matrix[0])
    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
