#Solution using recursion

import copy

def getSubsets(setz):

    def _getSubsets(setz, index):
        if index == -1:
            return [[]]

        old_subs = _getSubsets(setz,index-1)
        new_subs = []
        item = setz[index]
        for val in old_subs:
            new_subs.append(val)
            # new_subs.append(val.append(item)) ## List is mutable
            entry = copy.deepcopy(val)
            entry.append(item)
            new_subs.append(entry)
            
        return new_subs

    return _getSubsets(setz,len(setz)-1)

# Combinatorics Solution
def getSubsets2(aset):
    allSubsets = []
    max = 1 << len(aset)
    for k in range(max):
        subset = convertIntToSet(k, aset)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset




print(getSubsets([1,2,3])
print("\n")
print(getSubsets2([1,2,3]))
