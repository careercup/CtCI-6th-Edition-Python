#Solution using recursion

def getSubsets(setz, index):
    allSubsets = [[]]
    if len(setz) == index:
        #base case - add empty set
        allSubsets.append([])
    else:
        allSubsets = getSubsets(setz, index+1)
        item = setz[index]
        moreSubsets = [[]]
        for subset in allSubsets:
            newSubset = []
            [newSubset.append(value) for value in subset]
            newSubset.append(item)
            moreSubsets.append(newSubset)
        [allSubsets.append(value) for value in moreSubsets]
    return allSubsets

print(getSubsets([1,2,3],0))

