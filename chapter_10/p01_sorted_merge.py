def sorted_merge(a, b):
    index = len(a) - 1
    index_b = len(b) - 1
    index_a = len(a) - len(b) - 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1
        if index > 0:
            index -= 1
    return a


def fill_array_up_to(maxnum):
    return [2 * i + 4 for i in range(maxnum)]


def fill_array_with_buffer(length, buffer):
    return [3 * i + 1 for i in range(length)] + ([0] * buffer)


def test_sorted_merge():
    a = [9, 10, 11, 12, 13, 0, 0, 0, 0]
    b = [4, 5, 6, 7]
    expected = [4, 5, 6, 7, 9, 10, 11, 12, 13]
    assert sorted_merge(a, b) == expected


def example():
    a = fill_array_with_buffer(5, 10)
    b = fill_array_up_to(10)
    print(a, b)
    print(sorted_merge(a, b))


if __name__ == "__main__":
    example()
