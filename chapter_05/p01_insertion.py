def bits_insertion(n, m, i, j):
    """
    Accepts:
        m: str, representation of integer as binary string
        n: str, representation of integer as binary string
        i: int, ending bit position of number m for n
        j: int, starting bit position of number m for n
    Returns:
        str, representation of the number where n inserted into m
    """
    num_bits = len(m)  # determine number of characters for returned string
    ones = sum(2 ** _ for _ in range(num_bits))  # Generate all binary 1s
    ones_left = ones << (j + 1)  # shift 1s over to the left, before position j
    ones_right = (1 << i) - 1  # place 1s to the right of position i
    mask = ones_left | ones_right  # encapsulate 0s with the 1s from above
    cleared = int(n, 2) & mask  # zero bits in positions j through i
    moved = int(m, 2) << i  # shift m over i places, prepped for n insertion
    answer = cleared | moved  # answer is the value after insertion
    bit_str = ""  # format the answer number as a string of 0s and 1s
    # repeat dividing the answer by two until it reaches zero, or less than one
    # if the remainder is odd, prefix the bit string with '1', else '0'
    while answer:
        bit_str = "1" + bit_str if answer & 1 == 1 else "0" + bit_str
        answer //= 2
    return bit_str.zfill(num_bits)  # pad string to num_bits


def test_bits_insertion():
    assert bits_insertion("10000000000", "10011", 2, 6) == "10001001100"


if __name__ == "__main__":
    print(bits_insertion("10000000000", "10011", 2, 6))
