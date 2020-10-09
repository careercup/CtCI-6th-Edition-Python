"""
Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
eg:

Input: 3
Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
Hints: #138, #174, #187, #209, #243, #265, #295

"""
"""
# use hashmap, and build it 
# page 359 book
# approach 1
# This works, but it's not very efficient. We waste a lot of time coming up with the duplicate strings.

def helper(n):
    if n == 1:
        return ["()"]
    hashmap = {}
    combos = helper(n - 1)
    result = []
    for com in combos:
        for idx, char in enumerate(com):
            if char == "(":
                elem = insertParensAfter(com, idx)
                if elem not in hashmap:
                    result.append(elem)
                    hashmap[elem] = True
        elem = insertParensAfter(com, len(com) - 1)
        if elem not in hashmap:
            result.append(elem)
            hashmap[elem] = True
    return result

def insertParensAfter(string, idx):
    return string[:idx+1] + "()" + string[idx + 1:]

a = helper(4)
print(a)
"""

# approach 2
def addParen(arr, leftRem, rightRem, stringArr, idx):
    print("string arr", stringArr, "leftRem", leftRem, "rightRem", rightRem, "idx", idx)
    if leftRem < 0 or rightRem < leftRem:   # invalid
        return
    if leftRem == 0 and rightRem == 0:  # out of left and right parentheses
        elem = ''.join(stringArr)
        print(elem)
        arr.append(elem)
        
    else:
        stringArr[idx] = "("     # add left and recurse
        addParen(arr, leftRem - 1, rightRem, stringArr, idx + 1)
        
        stringArr[idx] = ")"     # add right and recurse
        addParen(arr, leftRem, rightRem - 1, stringArr, idx + 1)

def generateParens(n):
    arr = []
    stringArr = ["*"] * n * 2
    addParen(arr, n, n, stringArr, 0)
    return arr

a = generateParens(1)
print(a)

a = generateParens(2)
print(a)


# a = generateParens(3)
# print(a)



"""
for understanding purpose

string arr ['*', '*'] leftRem 1 rightRem 1 idx 0
string arr ['(', '*'] leftRem 0 rightRem 1 idx 1
string arr ['(', '('] leftRem -1 rightRem 1 idx 2
string arr ['(', ')'] leftRem 0 rightRem 0 idx 2
()
string arr [')', ')'] leftRem 1 rightRem 0 idx 1
['()']
string arr ['*', '*', '*', '*'] leftRem 2 rightRem 2 idx 0
string arr ['(', '*', '*', '*'] leftRem 1 rightRem 2 idx 1
string arr ['(', '(', '*', '*'] leftRem 0 rightRem 2 idx 2
string arr ['(', '(', '(', '*'] leftRem -1 rightRem 2 idx 3
string arr ['(', '(', ')', '*'] leftRem 0 rightRem 1 idx 3
string arr ['(', '(', ')', '('] leftRem -1 rightRem 1 idx 4
string arr ['(', '(', ')', ')'] leftRem 0 rightRem 0 idx 4
(())
string arr ['(', ')', ')', ')'] leftRem 1 rightRem 1 idx 2
string arr ['(', ')', '(', ')'] leftRem 0 rightRem 1 idx 3
string arr ['(', ')', '(', '('] leftRem -1 rightRem 1 idx 4
string arr ['(', ')', '(', ')'] leftRem 0 rightRem 0 idx 4
()()
string arr ['(', ')', ')', ')'] leftRem 1 rightRem 0 idx 3
string arr [')', ')', ')', ')'] leftRem 2 rightRem 1 idx 1
['(())', '()()']
"""
