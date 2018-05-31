class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise ValueError("Stack is empty")

        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]


def parse_equation(equation_str):
    terms = []
    operations = {"+", "/", "-", "*"}
    index = 0
    while index < len(equation_str):
        if equation_str[index] == " ":
            index += 1

        elif equation_str[index] not in operations:
            i = index + 1
            t = equation_str[index:i]
            while i < len(equation_str) and equation_str[i] not in operations:
                if equation_str[i] != " ":
                    t += equation_str[i]
                i += 1
            terms.append(t)
            index = i
        else:
            terms.append(equation_str[index])
            index += 1

    return terms


def collapse(a, b, operation):
    return eval(str(b) + operation + str(a))  # noqa


def calculate(s):
    terms = parse_equation(s)
    op_stack = Stack()
    num_stack = Stack()
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2}
    for x in terms:
        if x in priority.keys():
            if op_stack.is_empty() or priority[x] > priority[op_stack.peek()]:
                op_stack.push(x)
            else:
                while (
                    not op_stack.is_empty() and priority[x] <= priority[op_stack.peek()]
                ):
                    res = collapse(num_stack.pop(), num_stack.pop(), op_stack.pop())
                    num_stack.push(res)
                op_stack.push(x)

        else:
            num_stack.push(int(x))

    while not op_stack.is_empty():
        res = collapse(num_stack.pop(), num_stack.pop(), op_stack.pop())
        num_stack.push(res)

    return num_stack.pop()


def example():
    s = "2 -6 - 7 * 8 / 2 + 5"
    s1 = "2*3+5/6*3+15"

    print(s, "=>", calculate(s))
    print(s1, "=>", calculate(s1))


if __name__ == "__main__":
    example()
