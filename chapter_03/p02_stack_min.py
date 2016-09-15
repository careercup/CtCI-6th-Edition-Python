import sys


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [sys.maxsize] * (stacksize * self.numstacks)

    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise Exception("Stack is full")
        self.sizes[stacknum] += 1
        if self.is_empty(stacknum):
            self.minvals[self.index_of_top(stacknum)] = item
        else:
            self.minvals[self.index_of_top(stacknum)] = min(
                item, self.minvals[self.index_of_top(stacknum) - 1]
            )
        self.array[self.index_of_top(stacknum)] = item

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack is empty")
        value = self.array[self.index_of_top(stacknum)]
        self.array[self.index_of_top(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.index_of_top(stacknum)]

    def min(self, stacknum):
        return self.minvals[self.index_of_top(stacknum)]

    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def index_of_top(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


def StackMin():
    newstack = MultiStack(10)
    newstack.push(5, 0)
    newstack.push(6, 0)
    newstack.push(2, 0)
    newstack.push(7, 0)
    newstack.push(14, 0)
    newstack.push(3, 0)
    print(newstack.min(0))
    newstack.push(1, 0)
    newstack.push(4, 0)
    newstack.push(44, 0)
    newstack.push(2, 0)
    print(newstack.min(0))


if __name__ == "__main__":
    StackMin()
