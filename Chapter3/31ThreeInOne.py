class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.index_of_top(stacknum)] = item

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.index_of_top(stacknum)]
        self.array[self.index_of_top(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.index_of_top(stacknum)]

    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def index_of_top(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


def ThreeInOne():
    newstack = MultiStack(2)
    print newstack.is_empty(1)
    newstack.push(3, 1)
    print newstack.peek(1)
    print newstack.is_empty(1)
    newstack.push(2, 1)
    print newstack.peek(1)
    print newstack.pop(1)
    print newstack.peek(1)
    newstack.push(3, 1)

ThreeInOne()
