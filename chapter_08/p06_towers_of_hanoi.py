from collections import deque


# Custom Exceptions
class StackTooBigError(Exception):
    pass


class Stack:
    def __init__(self, stack_size) -> None:
        self.stack_size = stack_size
        self._stack = deque()

    def __str__(self):
        return " ".join(reversed([str(val) for val in self._stack]))

    def push(self, val):
        if len(self._stack) == self.stack_size:
            raise StackTooBigError("stack already reached max size")
        self._stack.append(val)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            raise IndexError("pop attempted from an empty stack")

    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            raise IndexError("top attempted from an empty stack")


class MultiStack:
    def __init__(self, stack_size, num_stacks=3):
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.multistack = [Stack(self.stack_size) for _ in range(self.num_stacks)]

    def get_stack(self, stack_num):
        if 0 > stack_num >= self.num_stacks:
            raise IndexError("stack_num invalid")
        return self.multistack[stack_num]

    def push(self, stack_num, val):
        return self.get_stack(stack_num).push(val)

    def top(self, stack_num):
        return self.get_stack(stack_num).top()

    def pop(self, stack_num):
        return self.get_stack(stack_num).pop()

    def __str__(self):
        str_result = [
            f"Stack {idx}\n{stack}" for idx, stack in enumerate(self.multistack)
        ]
        return "\n".join(str_result)

    def __repr__(self):
        return str(self)


class TowersOfHanoi:
    def __init__(self, stack_size, debug=False):
        self.stack_size = stack_size
        self.debug = debug
        self._stacks = MultiStack(stack_size)
        self.__init_first_stack()

    def __init_first_stack(self):
        for val in range(self.stack_size, 0, -1):
            self._stacks.push(0, val)

    def solve(self):
        if self.debug:
            print(f"Solving Towers of Hanoi - {self.stack_size} size")
        return self.__toh_solve(self.stack_size, 0, 1, 2)

    def __toh_solve(self, n, a, b, c):
        if n > 0:
            self.__toh_solve(n - 1, a, c, b)
            if self.debug:
                print(f"Plate {self._stacks.top(a)} -> Stack {c}")
            self._stacks.push(c, self._stacks.pop(a))
            self.__toh_solve(n - 1, b, a, c)

    def __str__(self):
        return str(self._stacks)

    def get_stack(self, stack_num):
        return self._stacks.get_stack(stack_num)._stack


if __name__ == "__main__":
    for test_case in range(1, 10):
        toh = TowersOfHanoi(test_case, debug=False)
        toh.solve()
        assert toh.get_stack(2) == deque(range(test_case, 0, -1))
        assert toh.get_stack(0) == toh.get_stack(1) == deque()
