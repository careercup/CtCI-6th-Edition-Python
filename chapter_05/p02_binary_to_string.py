def bin_to_string(number):
    bit_str = "."
    if number >= 1.0 or number <= 0.0:
        good_nums = ["1"] + ["1.0" + "0" * i for i in range(32)]
        good_nums += ["0"] + ["0.0" + "0" * i for i in range(32)]
        if str(number) not in good_nums:
            return "ERROR"
    while number > 0:
        if len(bit_str) > 32:
            return bit_str
        two = number * 2
        # Testing if 1 after decimal point
        if two >= 1:
            bit_str += "1"
            number = two - 1
        else:
            bit_str += "0"
            number = two
    return bit_str.ljust(33, "0")


def bin_to_string_alt(number):
    number_s31 = int(number * (2 ** 32))
    if number_s31 > 2 ** 32:
        return "ERROR"

    if number_s31 == (2 ** 32):
        number_s31 = 2 ** 32 - 1

    ans = ""
    for _ in range(32):
        ans = str(number_s31 % 2) + ans
        number_s31 = number_s31 // 2

    return "." + ans


def example():
    for number in [0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
        bit_str = bin_to_string(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        bit_str = bin_to_string_alt(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Number: {number}, Binary String: {response}")
        assert bin_to_string(number) == bin_to_string_alt(number)


if __name__ == "__main__":
    example()
