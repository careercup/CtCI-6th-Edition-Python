def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


def method_2(x):
    memo = [-1] * (x + 1)
    return triple_hop_recursive(x, memo)


def triple_hop_recursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]


if __name__ == "__main__":
    print(triple_hop(1))
    print(triple_hop(2))
    print(triple_hop(3))
    print(triple_hop(4))
    print(triple_hop(5))
    print(triple_hop(6))

    print(method_2(1))
    print(method_2(2))
    print(method_2(3))
    print(method_2(4))
    print(method_2(5))
    print(method_2(6))
