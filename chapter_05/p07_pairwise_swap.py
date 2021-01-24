def pairwise_swap(number):
    mask_10 = 0xAAAAAAAA  # 32 bits
    mask_01 = 0x55555555  # 32 bits
    num_evn = number & mask_10
    num_odd = number & mask_01
    swp_num = (num_evn >> 1) | (num_odd << 1)
    return swp_num


def test_pairwise_swap():
    view_output = 1
    for number, exp_output in zip([123, 781, 278], [183, 782, 553]):
        swap_num = pairwise_swap(number)
        if view_output:
            print(f"Number:  {bin(number)}")
            print(f"Swapped: {bin(swap_num)}")
        assert swap_num == exp_output


if __name__ == "__main__":
    test_pairwise_swap()
