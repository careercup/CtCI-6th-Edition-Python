# o(n) time
# o(n) space


def find_best_schedule(appointments):
    n = len(appointments)
    dp = [0] * (n + 1)
    dp[-2] = appointments[-1]

    max_so_far = -float("inf")

    for i in reversed(range(n - 1)):
        choices = []
        # choice 1, take the ith element, then skip i+1, and take i+2.
        choices.append((appointments[i] + dp[i + 2], i + 2))
        # choice 2, don't take ith element, the answer sits at dp[i+1]
        choices.append((dp[i + 1], i + 1))
        dp[i] = max(choices)[0]
        if dp[i] > max_so_far:
            max_so_far = dp[i]

    return max_so_far


def test_find_best_schedule():
    appointments = [30, 15, 60, 75, 45, 15, 15, 45]
    assert find_best_schedule(appointments) == 180
    appointments = [30, 15, 60, 15, 45, 15, 45]
    assert find_best_schedule(appointments) == 180
    appointments = [30, 15, 15, 60]
    assert find_best_schedule(appointments) == 90
