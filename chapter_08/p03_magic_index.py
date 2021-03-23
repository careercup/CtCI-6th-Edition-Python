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


def example():
    array = [-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]
    print(magic_index(array, 0, len(array) - 1))


if __name__ == "__main__":
    example()
