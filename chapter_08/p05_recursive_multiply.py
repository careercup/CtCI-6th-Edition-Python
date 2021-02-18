# naive implementation
def multiply(a, b, answer):
    if answer == 0 and a != 0 and b != 0:
        answer = a
    if a == 1:
        return answer

    if b == 1:
        return answer

    answer += a
    return multiply(a, b - 1, answer)


# Solution 1
def min_product(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    # Compute half. If uneven, compute other half. If even, double it
    s = smaller >> 1  # divide by 2
    side1 = min_product(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller - s, bigger)

    return side1 + side2


# Solution 2
def min_product_2(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_2_helper(smaller, bigger, {})


def min_product_2_helper(smaller, bigger, memo):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger

    if smaller in memo:
        return memo[smaller]

    # Compute half. If uneven, compute other half. If even double it
    s = smaller >> 1
    side1 = min_product_2_helper(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_2_helper(smaller - s, bigger, memo)
    # sum and cache
    memo[smaller] = side1 + side2
    return memo[smaller]


# Solution 3
def min_product_3(a, b):
    bigger = b if a < b else a  # a < b ? b : a
    smaller = a if a < b else b  # a < b ? a : b
    return min_product_3_helper(smaller, bigger)


def min_product_3_helper(smaller, bigger):
    if smaller == 0:
        return 0

    if smaller == 1:
        return bigger
    s = smaller >> 1
    half_prod = min_product_3_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod

    return half_prod + half_prod + bigger


# solution 4 # non-recursive
def multiply_bit_based(a, b):
    b_bin = bin(b)
    b_bin = b_bin[2:]
    prod = 0
    for i in range(len(b_bin)):  # O(len_b)
        if int(b_bin[-i - 1]):
            prod = prod + (a << i)

    return prod


test_cases = [(5, 6), (28, 89), (1234, 245334)]
testable_functions = [multiply_bit_based, min_product, min_product_2, min_product_3]


def test_min_product():
    for min_prod in testable_functions:
        for a, b in test_cases:
            assert min_prod(a, b) == a * b


if __name__ == "__main__":
    test_min_product()
