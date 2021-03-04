from typing import Optional


def _bit(x: int, i: int) -> int:
    return x & (1 << i)


def next_smaller(x: int) -> Optional[int]:
    if not x & (x + 1):
        return None
    zeros = ones = 0
    while _bit(x, i=ones):
        ones += 1
    while not _bit(x, i=ones + zeros):
        zeros += 1
    return x - (1 << ones) - (1 << zeros - 1) + 1


def next_larger(x: int) -> int:
    zeros = ones = 0
    while not _bit(x, i=zeros):
        zeros += 1
    while _bit(x, i=zeros + ones):
        ones += 1
    return x + (1 << zeros) + (1 << ones - 1) - 1


def test_next_smaller_than_0b11111() -> None:
    assert next_smaller(0b11111) is None


def test_next_smaller_than_0b10110() -> None:
    assert next_smaller(0b10110) == 0b10101


def test_next_larger_than_0b10110() -> None:
    assert next_larger(0b10110) == 0b11001


if __name__ == "__main__":
    x = int(input("Enter a positive integer: "))
    while x < 0:
        x = int(input(str(x) + " is not positive. Please try again: "))
    print("Next smaller: ", next_smaller(x))
    print("Next larger: ", next_larger(x))
