#Write a method to compute all permutations of a string of unique characters

# approach 1: building from permutations of first n-1 characters
def getPerms(string):
    permutations = []
    if string == None:
        return None
    if len(string) == 0:
        #base case
        permutations.append(" ")
        return permutations
    first = string[0] #get first letter in string
    remainder = string[1:]
    words = getPerms(remainder)
    for word in words:
        index = 0
        for letter in word:
            s = insertCharAt(word, first, index)
            permutations.append(s)
            index += 1
    return permutations

def insertCharAt(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end


# approach 2: Building from permutations of all n-1 character substrings
def getPerms2(string):
    result = []
    getPerms2Inner(" ", string, result)
    return result

def getPerms2Inner(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i+1:]
        c = remainder[i]
        getPerms2Inner(prefix + c, before + after, result)

print(getPerms("str"))
print(getPerms2("str"))
