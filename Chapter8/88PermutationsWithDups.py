def printPerms(string):
    result = []
    letterCountMap = buildFreqTable(string)
    printPermsInner(letterCountMap, "", len(string), result)
    return result

#returns dictionary <string, integer>
def buildFreqTable(string):
    letterCountMap = {}
    for letter in string:
        if letter not in letterCountMap:
            letterCountMap[letter] = 0
        letterCountMap[letter] += 1
    return letterCountMap

def printPermsInner(letterCountMap, prefix, remaining, result):
    #base case Permutation has been completed
    if remaining == 0:
        result.append(prefix)
        return
    #try remaining letter for next char, and generate remaining permutations
    for character in letterCountMap:
        count = letterCountMap[character]
        if count > 0:
            letterCountMap[character] -= 1
            printPermsInner(letterCountMap, prefix + character, remaining - 1, result)
            letterCountMap[character] = count

print(printPerms("aaf"))


