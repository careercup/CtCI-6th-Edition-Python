import sys


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
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

    def minimum(self, stacknum):
        return self.minvals[self.index_of_top(stacknum)]

    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def index_of_top(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def size(self, stacknum):
        return self.sizes[stacknum]


def f(n, start, end, buff, stack):
    if n == 1:
        stack.push(stack.pop(start), end)
    else:
        f(n - 1, start, buff, end, stack)
        f(1, start, end, buff, stack)
        f(n - 1, buff, end, start, stack)


def print_tower(newstack):
    # while not newstack.is_empty(0):
    # print(newstack.pop(0))
    # print("".join("-" for i in range(newstack.pop(0))))
    # while not newstack.is_empty(1):
    # print(newstack.pop(1))
    # print("".join("-" for i in range(newstack.pop(1))))
    while not newstack.is_empty(2):
        # print(newstack.pop(2))
        print("".join("-" for i in range(newstack.pop(2))))


def fill_tower(n):
    newstack = MultiStack(n * 3)
    for i in range(n, 0, -1):
        newstack.push(i, 0)
    return newstack


def example():
    n = 3
    newstack = fill_tower(n)
    f(n, 0, 2, 1, newstack)
    print_tower(newstack)


if __name__ == "__main__":
    example()
