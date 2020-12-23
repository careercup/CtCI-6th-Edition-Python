# Write a method to compute all permutations of a string of unique characters

# approach 1: building from permutations of first n-1 characters
def get_perms(string):
    permutations = []
    if string is None:
        return None
    if len(string) == 0:
        # base case
        permutations.append(" ")
        return permutations
    first = string[0]  # get first letter in string
    remainder = string[1:]
    words = get_perms(remainder)
    for word in words:
        index = 0
        for _ in word:
            s = insert_char_at(word, first, index)
            permutations.append(s)
            index += 1
    return permutations


def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end


# approach 2: Building from permutations of all n-1 character substrings
def get_perms_2(string):
    result = []
    get_perms_inner_2(" ", string, result)
    return result


def get_perms_inner_2(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_perms_inner_2(prefix + c, before + after, result)


if __name__ == "__main__":
    print(get_perms("str"))
    print(get_perms_2("str"))
