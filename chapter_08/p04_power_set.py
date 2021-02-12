import copy


# Solution using recursion
def get_subsets(setz, index=None):
    if index is None:
        index = len(setz) - 1
    if index == -1:
        return [[]]

    old_subs = get_subsets(setz, index - 1)
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


# alternative easier to understand recursive solution.
def get_subsets_3(s):
    cache = []  # holds all the subsets
    cache.append([])

    def recurse(cs, rs):  # cs is current, and rs is remaining.
        if len(rs) == 0:  # base case
            return

        for i in range(len(rs)):
            if cs + [rs[i]] not in cache:
                cache.append(cs + [rs[i]])
                recurse(cs + [rs[i]], rs[i + 1 :])

    recurse([], s)
    return cache


if __name__ == "__main__":
    print(get_subsets([1, 2, 3]))
    print("")
    print(get_subsets_2([1, 2, 3]))
    print("")
    print(get_subsets_3([1, 2, 3]))
