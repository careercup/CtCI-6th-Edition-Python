# O(NxN)
import unittest


def rotate(mat, dir='clockwise'):
    """ rotate a matrix 90 degrees clockwise or counter clockwise"""
    new = [[] for i in range(0,len(mat))]
    if dir == 'clockwise':
        for i in reversed(range(0,len(mat))):
            for j in range(0, len(mat[i])):
                new[j].append(mat[i][j])
    elif dir == 'counter_clockwise':
        for i in range(0,len(mat)):
            for j in range(0, len(mat[i])):
                new[(len(mat) -1 - j)].append(mat[i][j])
    return new




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate(test_matrix, 'clockwise')
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
