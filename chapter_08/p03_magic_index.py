import pytest


class NoMagicIndexExistsError(RuntimeError):
    pass


def magic_index(array, min_index=0, max_index=None):
    if max_index is None:
        max_index = len(array) - 1

    if max_index < min_index:
        raise NoMagicIndexExistsError("No magic index exists")

    mid = (max_index + min_index) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid + 1, max_index)
    if array[mid] > mid:
        return magic_index(array, min_index, mid - 1)


test_cases = [
    ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
    ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], NoMagicIndexExistsError),
    ([0, 1, 2, 3, 4], 2),
    ([], NoMagicIndexExistsError),
]

followup_test_cases = [
    ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 3),
]


def test_magic_index():
    for array, expected in test_cases:
        if isinstance(expected, int):
            assert magic_index(array) == expected
        else:
            with pytest.raises(expected):
                magic_index(array)


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
