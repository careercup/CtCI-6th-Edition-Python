import unittest


def swap_numbers_diff(a, b):
    a = b - a
    b = b - a  # = b-(b-a) = b-b+a = a
    a = a + b  # = (b-a)+a = b-a+a = b
    return a, b


def swap_numbers_xor(a, b):
    a = a ^ b
    b = a ^ b  # = (a^b)^b = a^(b^b) = a^0 = a
    a = a ^ b  # = (a^b)^(a) = a^b^a = b^(a^a) = b^0 = b
    return a, b


testable_functions = [swap_numbers_diff, swap_numbers_xor]

test_cases = [[1, 2], [10, 3], [4, 4], [1, 0], [7, -4], [-7, -4]]


class Test(unittest.TestCase):
    def test_small_big(self):
        for f in testable_functions:
            for a, b in test_cases:
                assert (b, a) == f(a, b)


if __name__ == "__main__":
    unittest.main()
