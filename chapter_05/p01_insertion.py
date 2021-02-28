def bits_insertion(n, m, i, j):
    ones = sum(2 ** _ for _ in range(m.bit_length()))  # Generate all binary 1s
    ones_left = ones << (j + 1)  # shift 1s over to the left, before position j
    ones_right = (1 << i) - 1  # place 1s to the right of position i
    mask = ones_left | ones_right  # encapsulate 0s with the 1s from above
    cleared = n & mask  # zero bits in positions j through i
    moved = m << i  # shift m over i places, prepped for n insertion
    return cleared | moved  # answer is the value after insertion


test_cases = [
    ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
    ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
]

testable_functions = [bits_insertion]


def test_bits_insertion():
    for bits_insert in testable_functions:
        for (n, m, i, j), expected in test_cases:
            calculated = bits_insert(n, m, i, j)
            error_msg = f"{bits_insert.__name__}: {calculated:b} != {expected:b}"
            assert bits_insert(n, m, i, j) == expected, error_msg


if __name__ == "__main__":
    test_bits_insertion()
