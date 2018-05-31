ones = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Tweleve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eigteen",
    "Nineteen",
]

twos = {
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
}

threes = ["", "Thousand", "Million", "Billion"]


def get_chunks(n):
    result = []

    if 1 <= (n % 100) < 20:
        result.append(ones[(n % 100) - 1])

    elif 20 <= (n % 100) < 100:
        if (n % 10) != 0:
            result.append(ones[n % 10 - 1])
        result.insert(0, twos.get((n % 100 - n % 10), ""))

    if n >= 100:
        result = [ones[n // 100 - 1], "Hundred"] + result

    return result


def get_in_words(n):
    if n == 0:
        return "Zero"

    int_in_words = []
    index = 0

    while n > 0:
        temp = n % 1000
        res = get_chunks(temp)
        if res:
            int_in_words = res + [threes[index]] + int_in_words
        index += 1
        n //= 1000

    return " ".join(int_in_words)


def example():
    nums = [
        1,
        10,
        13,
        19,
        20,
        23,
        50,
        73,
        93,
        100,
        101,
        110,
        119,
        195,
        300,
        504,
        950,
        974,
        999,
        1000,
        10000,
        909000,
        1000000,
        9000009,
        19323984,
        908900034,
        100000000781,
    ]

    for n in nums:
        print(n, get_in_words(n))


if __name__ == "__main__":
    example()
