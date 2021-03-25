# o(k^2) algo
def get_kth_multiple(k):
    res = [1, 3, 5, 7]
    is_number_seen = {1, 3, 5}
    if k <= 3:
        return res[k]

    for i in range(k - 3):
        choices = []
        for j in range(len(res)):
            if 3 * res[j] not in is_number_seen:
                choices.append(3 * res[j])
            if 5 * res[j] not in is_number_seen:
                choices.append(5 * res[j])
            if 7 * res[j] not in is_number_seen:
                choices.append(7 * res[j])
        ans = min(choices)
        res.append(ans)

        is_number_seen.add(ans)

    return res[-1]


def get_kth_multiple_via_heap(k):
    res = []
    is_number_seen = set()
    import heapq

    heap = [3, 5, 7]
    heapq.heapify(heap)
    for i in range(k):
        next_el = heapq.heappop(heap)
        # is_number_seen.add(next_el)
        res.append(next_el)
        if (next_el * 3) not in is_number_seen:
            is_number_seen.add(next_el * 3)
            heapq.heappush(heap, next_el * 3)
        if (next_el * 5) not in is_number_seen:
            is_number_seen.add(next_el * 5)
            heapq.heappush(heap, next_el * 5)
        if (next_el * 7) not in is_number_seen:
            is_number_seen.add(next_el * 7)
            heapq.heappush(heap, next_el * 7)
    print(res)
    return res[-1]


test_cases = [
    # k, expected
    (1, 3),
    (2, 5),
    (3, 7),
    (1000, 82046671875),
]

testable_functions = [get_kth_multiple_via_heap]


def test_kth_multiple():
    for f in testable_functions:
        for k, expected in test_cases:
            assert f(k) == expected


if __name__ == "__main__":
    test_kth_multiple()
