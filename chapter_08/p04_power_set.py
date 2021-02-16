import copy


# Solution using recursion
def get_subsets_a(setz, index=None):
    if index is None:
        index = len(setz) - 1
    if index == -1:
        return [[]]

    old_subs = get_subsets_a(setz, index - 1)
    new_subs = []
    item = setz[index]
    for val in old_subs:
        new_subs.append(val)
        # List is mutable
        entry = copy.deepcopy(val)
        entry.append(item)
        new_subs.append(entry)

    return new_subs


# Combinatorics Solution
def get_subsets_b(aset):
    all_subsets = []
    max_n = 1 << len(aset)
    for k in range(max_n):
        subset = convert_int_to_set(k, aset)
        all_subsets.append(subset)
    return all_subsets


def convert_int_to_set(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset


# alternative recursive solution.
def get_subsets_c(_set):
    subsets = [[]]

    def recurse(current_set, remaining_set):
        if len(remaining_set) == 0:  # base case
            return

        for i in range(len(remaining_set)):
            if current_set + [remaining_set[i]] not in subsets:
                subsets.append(current_set + [remaining_set[i]])
                recurse(current_set + [remaining_set[i]], remaining_set[i + 1 :])

    recurse([], _set)
    return subsets


testable_functions = [get_subsets_a, get_subsets_b, get_subsets_c]

test_cases = [({1, 2, 3}, {(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)})]


def test_get_subsets():
    for input_set, expected in test_cases:
        for get_subsets in testable_functions:
            results = get_subsets(list(input_set))
            results = {tuple(s) for s in results}
            assert results == expected


if __name__ == "__main__":
    print(get_subsets_a([1, 2, 3]))
    print("")
    print(get_subsets_b([1, 2, 3]))
    print("")
    print(get_subsets_c([1, 2, 3]))
