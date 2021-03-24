def find_max_people(height_weight_pairs):
    if not height_weight_pairs:
        return 0
    # sort on second dimension in decreasing order
    height_weight_pairs.sort(key=lambda x: -x[1])
    # then, problem is lis in first dimension
    dp = [float("inf") for _ in range(len(height_weight_pairs))]
    dp[0] = 1
    max_so_far = 1
    for i in range(1, len(height_weight_pairs)):
        # look at the elements in the range [0,i-1] (does not include i)
        choices = [1]
        for j in range(0, i):
            if height_weight_pairs[i][0] < height_weight_pairs[j][0]:
                # then feasible candidate
                choices.append(1 + dp[j])
        dp[i] = max(choices)
        max_so_far = max(max_so_far, dp[i])
    return max_so_far


test_cases = [
    # height_weight_pairs, expected_length
    ([], 0),
    ([(65, 100), (100, 65)], 1),
    ([(65, 100), (65, 100)], 1),
    ([(65, 100), (65, 101)], 1),
    ([(65, 100), (55, 40), (75, 90), (80, 120)], 3),
    ([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)], 6),
]


def test_circus_tower():
    for height_weight_pairs, expected_length in test_cases:
        assert find_max_people(height_weight_pairs) == expected_length
