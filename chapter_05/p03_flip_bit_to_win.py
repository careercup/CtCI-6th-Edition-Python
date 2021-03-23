def flip_bit_to_win(number):
    number_str = bin(number)[2:]
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(number_str)  # start index
    while i:
        if int(number_str[i - 1]):
            cnt += 1
        else:
            if cnt0 == 0:
                temp_i = i
                cnt0 = 1
            else:  # second 0
                max_cnt = cnt
                i = temp_i  # rewind
                cnt0 = 0
                cnt = 0
        i -= 1

    max_cnt = max(cnt, max_cnt)

    return max_cnt + 1


test_cases = [(0b0, 1), (0b111, 4), (0b11011101111, 8)]


def test_flip_bit_to_win():
    for num, expected in test_cases:
        assert flip_bit_to_win(num) == expected


if __name__ == "__main__":
    test_flip_bit_to_win()
