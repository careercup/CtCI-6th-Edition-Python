
```
def generateParenthesis( n ) :
    listOfParens = []
    if n == 1:
        listOfParens.append('()')
        return listOfParens
    rem = generateParenthesis(n - 1)
    for paren in rem:
        for i in range(len(paren) + 1):
            s = paren[ : i] + '()' + paren[i : ]
            if s not in listOfParens:
                listOfParens.append(s)
    return listOfParens
    
print(generateParenthesis( 3 ))

```
