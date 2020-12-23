# Solution using recursion


def get_subsets(setz, index):
    all_subsets = []
    if len(setz) == index:
        # base case - add empty set
        if [] not in all_subsets:
            all_subsets.append([])
    else:
        all_subsets = get_subsets(setz, index + 1)
        item = setz[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            for value in subset:
                if value not in new_subset:
                    new_subset.append(value)

            new_subset.append(item)
            more_subsets.append(new_subset)
        for value in more_subsets:
            if value not in new_subset:
                all_subsets.append(value)

    return all_subsets


# Combinatorics Solution
def get_subsets_2(aset):
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


if __name__ == "__main__":
    print(get_subsets([1, 2, 3], 0))
    print("\n")
    print(get_subsets_2([1, 2, 3]))
