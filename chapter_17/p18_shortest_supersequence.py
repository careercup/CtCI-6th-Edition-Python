#o(n) time, o(n) space solution via sliding window.
#better than the one provided in ctci.

#find the smallest substring in s, which matches t.
import collections
def minWindow(s: str, t: str) -> str:
    m, n = len(s), len(t)
    hash = collections.defaultdict(int)
    # store frequencies in hash
    for i in range(n):
        hash[t[i]] += 1

    # window invariant: 'contains all the chars in t'
    min_win_len = float("inf")
    left = 0
    missing = n
    min_win_left = -1
    min_win_right = -1
    for right, char in enumerate(s):
        # insertion logic
        if hash[char] > 0:
            missing -= 1
        # nevertheless, insert the element
        hash[char] -= 1

        if missing == 0:

            while left <= right and missing == 0:
                if right - left + 1 < min_win_len:
                    min_win_len = right - left + 1
                    min_win_left = left
                    min_win_right = right

                if hash[s[left]] == 0:
                    # then you are making a blunder
                    missing += 1
                    hash[s[left]] += 1
                    left += 1
                    # break
                else:
                    hash[s[left]] += 1
                    left += 1

    if min_win_len == float("inf"): return 
    print(min_win_left,min_win_right)

s = "75902135791158897"
t = "159"
minWindow(s,t)