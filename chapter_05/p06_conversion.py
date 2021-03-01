import unittest


def bit_swap_required(a: int, b: int) -> int:
    count, c = 0, a ^ b
    while c:
        count, c = count + 1, c & (c - 1)
    return count


class TestBitSwapRequired(unittest.TestCase):
    def test_29_15(self) -> None:
        a = 0b11101  # 29
        b = 0b01111  # 15
        self.assertEqual(2, bit_swap_required(a, b))


if __name__ == "__main__":
    unittest.main()
