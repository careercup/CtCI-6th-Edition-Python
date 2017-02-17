"""Two 32-bit numbers N, M; two bit positions i, j.
Insert M into N such that M starts at j and ends at i. j > i.
Can assume it will fit.

Using string slices.  e.g. insert:
        [  -4 -1   ]
m =     [   1101   ]        (dec 13) into
n =     [1000000000] len=10 (dec 512) gives
        [1001101000] len=10 (dec 616)
i,j,x = [   7  4  1]
"""

from collections import deque


def fit(n, m, i, j):
    n_repr = bin(n)[2:]  # strip leading 0b
    print("n:", n_repr)
    m_repr = bin(m)[2:]
    print("m:", m_repr)
    new = deque()
    for x in range(1, len(n_repr) + 1):  # 1..i, j
        if x >= i and x <= j:
            new.appendleft(m_repr[-1 * (x - i) - 1])
        else:
            new.appendleft(n_repr[-1 * x])
    new.extendleft(["b", "0"])
    s = "".join(new)
    print("s:", s)
    return int(s, 2)

print("Expect 616:", fit(512, 13, 4, 7))
