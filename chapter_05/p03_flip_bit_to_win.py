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


def flip_bit_to_win_alt(num):
    longest, current_segment, past_segment = 1, 0, 0
    while num != 0:
        if num & 1:  # Current bit is 1
            current_segment += 1
        else:  # Current bit is 0
            past_segment = 0 if (num & 2 is True) else current_segment
            current_segment = 0
        longest = max(current_segment + past_segment + 1, longest)
        num >>= 1  # Move 1 bit to the right
    return longest


def test_flip_bit_to_win():
    test_in = [7, 1775]
    test_out = [4, 8]
    for i, o in zip(test_in, test_out):
        assert flip_bit_to_win(i) == o
        assert flip_bit_to_win_alt(i) == o


if __name__ == "__main__":
    test_flip_bit_to_win()
