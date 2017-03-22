STANDARD_COIN_SIZES = [1, 5, 10, 20, 25]


def coin_combinations(amount, coin_sizes=None):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if coin_sizes is None:
        coin_sizes = STANDARD_COIN_SIZES

    if len(coin_sizes) == 0:
        return 0
    m = len(coin_sizes)
    return coin_combinations(amount, coin_sizes[: m - 1]) + coin_combinations(
        amount - coin_sizes[m - 1], coin_sizes
    )


def coin_combinations_iterative(amount, coin_sizes=None):
    table = [0] * (amount + 1)
    # first case 0 value
    table[0] = 1

    if coin_sizes is None:
        coin_sizes = STANDARD_COIN_SIZES
    for i in range(0, len(coin_sizes)):
        for j in range(coin_sizes[i], amount + 1):
            table[j] += table[j - coin_sizes[i]]
    return table[amount]


if __name__ == "__main__":
    print(coin_combinations(100))
    print(coin_combinations_iterative(100))
