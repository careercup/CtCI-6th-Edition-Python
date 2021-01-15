import unittest


def string_to_bool(s: str) -> bool:
    return s == "1"


def count_ways(exp: str, result: bool, memo) -> int:
    if len(exp) == 0:
        return 0
    if len(exp) == 1:
        return 1 if string_to_bool(exp) == result else 0

    if exp + str(result) in memo:
        return memo[exp + str(result)]

    ways = 0
    for i in range(1, len(exp), 2):
        left = exp[:i]
        right = exp[i + 1 :]

        left_true = count_ways(left, True, memo)
        left_false = count_ways(left, False, memo)
        right_true = count_ways(right, True, memo)
        right_false = count_ways(right, False, memo)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if exp[i] == "|":
            total_true = (
                left_true * right_true
                + left_false * right_true
                + left_true * right_false
            )
        elif exp[i] == "&":
            total_true = left_true * right_true
        elif exp[i] == "^":
            total_true = left_true * right_false + left_false * right_true

        subways = total_true if result else (total - total_true)
        ways += subways

    memo[exp + str(result)] = ways
    return ways


def evaluate(exp: str, result: bool) -> int:
    memo = {}
    return count_ways(exp, result, memo)


class Test(unittest.TestCase):
    test_cases = [("1^0|0|1", False, 2), ("0&0&0&1^1|0", True, 10)]
    testable_functions = [evaluate]

    def test_evaluate(self):
        for f in self.testable_functions:
            for [expression, result, expected] in self.test_cases:
                assert f(expression, result) == expected


if __name__ == "__main__":
    unittest.main()
