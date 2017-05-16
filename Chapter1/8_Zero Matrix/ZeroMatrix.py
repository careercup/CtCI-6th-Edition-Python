# O(MxN)
import unittest


def zero_matrix(matrix):
    """ fill rows and columns with zeros if they contain a zero"""
    i_0s = []
    j_0s = []
    for i_index, i in enumerate(matrix):
        for j_index, j in enumerate(i):
            if j == 0:
                i_0s.append(i_index)
                j_0s.append(j_index)
    for i_index, i in enumerate(matrix):
        if i_index in i_0s:
            matrix[i_index] = [0 for pos in i]
        else:
            for j_index in range(0, len(i)):
                if j_index in j_0s:
                    matrix[i_index][j_index] = 0
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
