import sys


# Function to sort the arrays in O(nlog(n))
def merge_sort(arr):
    # function to create the partitions
    def make_partition(_arr):
        if len(_arr) <= 1:
            return _arr
        middle = len(_arr) // 2
        left = make_partition(_arr[:middle])
        right = make_partition(_arr[middle:])

        return merge_partition(left, right)

    # function to merge the array partitions
    def merge_partition(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]
        return result

    return make_partition(arr)


# Function to find the smallest difference
def find_smallest_difference(array1, array2):
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    a, b, difference = 0, 0, sys.maxsize
    pair = []

    while a < len(array1) and b < len(array2):
        if abs(array1[a] - array2[b]) < difference:
            difference = abs(array1[a] - array2[b])
            pair = [array1[a], array2[b]]
        if array1[a] < array2[b]:
            a += 1
        else:
            b += 1

    return difference, pair


def test_find_smallest_diff():
    test_cases = [
        [[1, 3, 15, 11, 2], [23, 127, 235, 19, 8], (3, [11, 8])],
        [[2, 11, 15, 1], [12, 4, 235, 19, 127, 23], (1, [11, 12])],
    ]
    for a, b, expected in test_cases:
        assert find_smallest_difference(a, b) == expected
