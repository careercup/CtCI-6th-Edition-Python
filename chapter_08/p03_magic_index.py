def magic_index(array, min_index, max_index):
    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid + 1, max_index)
    if array[mid] > mid:
        return magic_index(array, min_index, mid - 1)

    raise Exception("Not possible")


def magic_index_non_distinct(array, min_index, max_index):
    if max_index < min_index:
        return -1

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid

    # Search left recursively
    left_index = min(mid - 1, array[mid])
    left = magic_index_non_distinct(array, min_index, left_index)
    if left >= 0:
        return left

    # Search right recursively
    right_index = max(mid + 1, array[mid])
    right = magic_index_non_distinct(array, right_index, max_index)
    if right >= 0:
        return right


def example_magic_index():
    array = [-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]
    print(magic_index(array, 0, len(array) - 1))


def example_magic_index_non_distinct():
    array = [-10, -5, 1, 3, 3, 3, 4, 7, 9, 12, 13]
    print(magic_index_non_distinct(array, 0, len(array) - 1))


if __name__ == "__main__":
    example_magic_index()
    example_magic_index_non_distinct()
