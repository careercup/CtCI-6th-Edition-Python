import unittest


def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return True


def is_matched_parentheses(ray):
    lst = []
    for c in ray:
        if c == "(":
            lst.append(c)
        if c == ")":
            if len(lst) < 1 or lst.pop() != "(":
                return False
    return True


def generate_parentheses_permutations_brute_force(number_of_pairs):
    starting_list = (["("] * number_of_pairs) + [")"] * number_of_pairs
    possibilities = ["".join(starting_list)]
    while next_permutation(starting_list):
        if is_matched_parentheses(starting_list):
            possibilities.append("".join(starting_list))
    return possibilities


def generate_parentheses_permutations(n):
    def helper(
        open_parentheses_remaining, closed_parentheses_remaining, current_string
    ):
        if len(current_string) == n * 2:
            result.append(current_string)
        if open_parentheses_remaining > 0:
            helper(
                open_parentheses_remaining - 1,
                closed_parentheses_remaining,
                current_string + "(",
            )
        if closed_parentheses_remaining > open_parentheses_remaining:
            helper(
                open_parentheses_remaining,
                closed_parentheses_remaining - 1,
                current_string + ")",
            )

    result = []
    helper(n, n, "")
    return result


testable_functions = [
    generate_parentheses_permutations_brute_force,
    generate_parentheses_permutations,
]

test_cases = [
    (0, [""]),
    (1, ["()"]),
    (2, sorted(["()()", "(())"])),
    (3, sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])),
]


class TestSuite(unittest.TestCase):
    def test_generate_parentheses_permutations(self):
        for f in testable_functions:
            for num, expected in test_cases:
                self.assertEqual(sorted(f(num)), expected)


def example():
    print(generate_parentheses_permutations(2))
    print(generate_parentheses_permutations_brute_force(3))


if __name__ == "__main__":
    example()
