"""
Exercise: 16.26 Calculator
Given a matrix representation of plot of land, find the sizes of all the ponds in the matrix.
0 indicates the water. Pond is the regionof water connected vertically, horizontally or diagonally.
"""

 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack == []:
            raise ValueError ('Stack is empty')

        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]


def parse_equation(s):
    l = []
    operations = set(['+', '/', '-', '*'])
    index = 0
    while index < len(s):
        if s[index] == ' ':
            index += 1

        elif s[index] not in operations:
            i = index+1
            t = s[index:i]
            while i< len(s) and s[i] not in operations:
                if s[i] != ' ':
                    t += s[i]
                i += 1
            l.append(t)
            index = i
        else:
            l.append(s[index])
            index += 1

    return l


def collapse(a, b, operation):
    return eval(str(b) + operation + str(a))


def calculate(s):
    l = parse_equation(s)
    op_stack = Stack()
    num_stack = Stack()
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    for x in l:
        if x in priority.keys():
            if op_stack.is_empty() or priority[x] > priority[op_stack.peek()]:
                op_stack.push(x)
            else:
                while not op_stack.is_empty() and priority[x] <= priority[op_stack.peek()]:
                    res = collapse(num_stack.pop(), num_stack.pop(), op_stack.pop())
                    num_stack.push(res)
                op_stack.push(x)
                
        else:
            num_stack.push(int(x))

    while not op_stack.is_empty():
        res = collapse(num_stack.pop(), num_stack.pop(), op_stack.pop())
        num_stack.push(res)

    return num_stack.pop()


if __name__ == "__main__":
    s = '2 -6 - 7 * 8 / 2 + 5'
    s1 = '2*3+5/6*3+15'

    print(s, '=>',calculate(s))
    print(s1, '=>', calculate(s1))

