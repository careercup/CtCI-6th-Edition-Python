from Stacks import Stack

class StackWithMin(Stack):

    def __init__(self):
        self.s2 = Stack()
        super().__init__()

    def min(self):
        if self.s2.isEmpty():
            return 1000000
        else:
            return self.s2.peek()

    def push(self, item):
        if item < self.min():
            self.s2.push(item)
        super().push(item)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.s2.pop()

        return value


stk = StackWithMin()

stk.push(5)
print(stk.min())
stk.push(6)
print(stk.min())
stk.push(3)
print(stk.min())
stk.push(7)
print(stk.min())
stk.pop()
print(stk.min())
stk.pop()
print(stk.min())

