def sparse_search(arr, item):
    def inner_search(arr, item, low, high):
        middle = ((high - low) // 2) + low

        if arr[middle] == "":
            left = middle - 1
            right = middle + 1
            while True:
                if left < low and right > high:
                    return None
                elif right <= high and arr[right] != "":
                    middle = right
                    break
                elif left >= low and arr[left] != "":
                    middle = left
                    break
                left -= 1
                right += 1

        if arr[middle] == item:
            return middle
        if arr[middle] > item:
            return inner_search(arr, item, low, middle - 1)
        if arr[middle] < item:
            return inner_search(arr, item, middle + 1, high)

    return inner_search(arr, item, 0, len(arr) - 1)


test_cases = [
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "d"), 8),
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "f"), None),
    ((["a", "", "", "b", "", "c", "", "", "d", "", "", "", "", "e", ""], "a"), 0),
]

testable_functions = [sparse_search]


def test_sorted_search():
    for function in testable_functions:
        for (n, m), expected in test_cases:
            calculated = function(n, m)
            error_msg = f"{function.__name__}: {calculated} != {expected}"
            assert function(n, m) == expected, error_msg


if __name__ == "__main__":
    test_sorted_search()
