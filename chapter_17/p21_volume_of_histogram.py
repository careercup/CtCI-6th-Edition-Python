# volume of histogram
# o(n) time
# o(n) space


def find_volume(a):
    if len(a) <= 2:
        return 0
    n = len(a)
    h_left = [0] * n  # max height on left, excluding the curr bar
    h_right = [0] * n  # max height on right, excluding the curr bar
    for i in range(1, n):
        h_left[i] = max(h_left[i - 1], a[i - 1])
    for i in reversed(range(n - 1)):
        h_right[i] = max(h_right[i + 1], a[i + 1])
    volume = 0
    # neglect extreme left and extreme right bar, they can never be filled
    for i in range(1, n - 1):
        min_height = min(h_left[i], h_right[i])
        if min_height - a[i] > 0:
            volume += min_height - a[i]

    return volume


def test_find_volume():
    hist = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
    assert find_volume(hist) == 26
