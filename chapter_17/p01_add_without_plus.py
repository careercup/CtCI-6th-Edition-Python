def add_without_plus(a, b):
    while b != 0:
        # Sum without carry bit
        _sum = a ^ b

        # Sum with only carrying
        carry = (a & b) << 1

        a = _sum
        b = carry

    return a


def add_without_plus_recursive(addend_a, addend_b):
    if addend_b == 0:
        return addend_a

    _sum = addend_a ^ addend_b
    carry = (addend_a & addend_b) << 1

    return add_without_plus_recursive(_sum, carry)


testable_functions = [add_without_plus_recursive, add_without_plus]

test_cases = [
    # a, b, expected
    (1, 1, 2),
    (1, 2, 3),
    (1001, 234, 1235),
    (123456789, 123456789, 123456789 * 2),
    # does not work with negatives :(
]


def test_add_without_plus():
    for f in testable_functions:
        for a, b, expected in test_cases:
            assert f(a, b) == expected
