def pairwise_swap(number):
    bin_str = bin(number)[2:]
    mask_10 = 0xAAAAAAAA  # 32 bits
    mask_01 = 0x55555555  # 32 bits
    num_evn = number & mask_10
    num_odd = number & mask_01
    swp_num = (num_evn >> 1) | (num_odd << 1)
    return swp_num


def example():
    for number in [123, 781, 278]:
        swap_num = pairwise_swap(number)
        print(f"Number:  {bin(number)}")
        print(f"Swapped: {bin(swap_num)}")


if __name__ == "__main__":
    example()
