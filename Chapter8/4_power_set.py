#Solution using recursion

def getSubsets(setz, index):
    allSubsets = []
    if len(setz) == index:
        #base case - add empty set
        if [] not in allSubsets:
            allSubsets.append([])
    else:
        allSubsets = getSubsets(setz, index+1)
        item = setz[index]
        moreSubsets = []
        for subset in allSubsets:
            newSubset = []
            [newSubset.append(value) for value in subset if value not in newSubset]
            newSubset.append(item)
            moreSubsets.append(newSubset)
        [allSubsets.append(value) for value in moreSubsets if value not in newSubset]
    return allSubsets

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




print(getSubsets([1,2,3],0))
print("\n")
print(getSubsets2([1,2,3]))
