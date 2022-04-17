from abc import abstractmethod
from collections import deque


class Stack:
    def __init__(self, stack_size) -> None:
        self.stack_size = stack_size
        self.stack = deque()

    def __str__(self):
        return " ".join(reversed([str(val) for val in self.stack]))

    def push(self, val):
        if len(self.stack) == self.stack_size:
            return
        self.stack.append(val)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        return None

    def top(self):
        if len(self.stack):
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def get_stack(self):
        return self.stack


class MultiStack:
    def __init__(self, stack_size, num_stacks=3):
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.multistack = [Stack(self.stack_size) for _ in range(self.num_stacks)]

    def __stack_num_check(f):
        def wrapper(self, *args):
            if args[0] >= self.num_stacks or args[0] < 0:
                raise Exception("stack_num invalid")
            return f(self, *args)

        return wrapper

    @__stack_num_check
    def push(self, stack_num, val):
        return self.multistack[stack_num].push(val)

    @__stack_num_check
    def top(self, stack_num):
        return self.multistack[stack_num].top()

    @__stack_num_check
    def pop(self, stack_num):
        return self.multistack[stack_num].pop()

    @__stack_num_check
    def is_empty(self, stack_num):
        return self.multistack[stack_num].is_empty()

    @__stack_num_check
    def show_stack(self, stack_num):
        print(str(self.multistack[stack_num]))

    @__stack_num_check
    def get_stack(self, stack_num):
        return self.multistack[stack_num].get_stack()

    def __str__(self):
        str_result = ""
        idx = 0
        for stack in self.multistack:
            str_result += f"Stack {idx}\n"
            str_result += str(stack) + "\n"
            idx += 1
        return str_result

    def __repr__(self):
        return str(self)


class TOH:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stacks = MultiStack(stack_size)
        self.__init_first_stack()

    def __init_first_stack(self):
        for val in range(self.stack_size, 0, -1):
            self.stacks.push(0, val)

    def solve(self, debug=True):
        self.debug = debug
        return self.__toh_solve(self.stack_size, 0, 1, 2)

    def __toh_solve(self, n, a, b, c):
        if n > 0:
            self.__toh_solve(n - 1, a, c, b)
            if self.debug:
                print(f"{self.stacks.top(a)} -> Stack {c}")
            self.stacks.push(c, self.stacks.pop(a))
            self.__toh_solve(n - 1, b, a, c)

    def print_stacks(self):
        print(self.stacks)

    def get_stack(self, stack_num):
        return self.stacks.get_stack(stack_num)


if __name__ == "__main__":
    for test_case in range(1, 10):
        toh = TOH(test_case)
        toh.solve(debug=False)
        assert toh.get_stack(2) == deque(list(range(test_case, 0, -1)))
        assert toh.get_stack(0) == toh.get_stack(1) == deque()
