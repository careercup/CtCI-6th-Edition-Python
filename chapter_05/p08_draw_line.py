def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    left_byte, right_byte = (y * width + x1) // 8, (y * width + x2) // 8
    left_mask, right_mask = 0xFF >> x1 % 8, (0xFF >> x2 % 8 + 1) ^ 0xFF
    if left_byte == right_byte:
        screen[left_byte] |= left_mask & right_mask
    else:
        screen[left_byte] |= left_mask
        for i in range(left_byte + 1, right_byte):
            screen[i] = 0xFF
        screen[right_byte] |= right_mask


def test_0b11111111_0b11111111() -> None:
    screen = bytearray(2)
    draw_line(screen, width=16, x1=0, x2=15, y=0)
    assert screen == bytearray([0b11111111, 0b11111111])


def test_0b01111100() -> None:
    screen = bytearray(1)
    draw_line(screen, width=8, x1=1, x2=5, y=0)
    assert screen == bytearray([0b01111100])


def test_0b01111100_with_y_equals_1() -> None:
    screen = bytearray(3)
    draw_line(screen, width=8, x1=1, x2=5, y=1)
    assert screen == bytearray([0b00000000, 0b01111100, 0b000000000])


def test_0b00000011_0b11111111_0b11000000() -> None:
    screen = bytearray(3)
    draw_line(screen, width=24, x1=6, x2=17, y=0)
    assert screen == bytearray([0b00000011, 0b11111111, 0b11000000])
