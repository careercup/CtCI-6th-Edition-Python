def magic_index(array, min, max):
    mid = (max + min) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return magic_index(array, mid + 1, max)
    if array[mid] > mid:
        return magic_index(array, min, mid - 1)

    raise Exception("Not possible")


def example():
    array = [-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]
    print(magic_index(array, 0, len(array) - 1))


if __name__ == "__main__":
    example()
