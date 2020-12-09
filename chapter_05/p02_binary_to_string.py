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


if __name__ == "__main__":

    for number in [0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
        bit_str = bin_to_string(number)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print("Number: {}, Binary String: {}".format(number, response))
