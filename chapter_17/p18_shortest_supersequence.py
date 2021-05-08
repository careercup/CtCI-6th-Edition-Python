# o(n) time, o(n) space solution via sliding window.
# better than the one provided in ctci.

import collections


def min_window(big_array, small_array):
    n = len(small_array)
    frequencies = collections.defaultdict(int)

    for i in range(n):
        frequencies[small_array[i]] += 1

    # window invariant: 'contains all the chars in t'
    min_win_len = float("inf")
    left = 0
    missing = n
    min_win_left = -1
    min_win_right = -1
    for right, char in enumerate(big_array):
        # insertion logic
        if frequencies[char] > 0:
            missing -= 1
        # nevertheless, insert the element
        frequencies[char] -= 1

        if missing == 0:

            while left <= right and missing == 0:
                if right - left + 1 < min_win_len:
                    min_win_len = right - left + 1
                    min_win_left = left
                    min_win_right = right

                if frequencies[big_array[left]] == 0:
                    # then you are making a blunder
                    missing += 1
                    frequencies[big_array[left]] += 1
                    left += 1
                    # break
                else:
                    frequencies[big_array[left]] += 1
                    left += 1

    if min_win_len == float("inf"):
        return
    return min_win_left, min_win_right


def test_min_window():
    s = "75902135791158897"
    t = "159"
    assert min_window(s, t) == (7, 10)
