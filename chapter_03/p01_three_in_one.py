import pytest


class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.array = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def push(self, value, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_full(stack_num):
            raise StackFullError(f"Push failed: stack #{stack_num} is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot pop from empty stack #{stack_num}")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f"Cannot peek at empty stack #{stack_num}")
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.number_of_stacks:
            raise StackDoesNotExistError(f"Stack #{stack_num} does not exist")


class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""


def test_multistack():
    num_stacks = 3
    stack_size = 6
    s = MultiStack(stack_size=stack_size, number_of_stacks=num_stacks)

    for stack_num in range(num_stacks):
        assert s.is_empty(stack_num)
        assert not s.is_full(stack_num)
        with pytest.raises(StackEmptyError):
            s.pop(stack_num)

        for i in range(stack_size - 1):
            s.push(i, stack_num=stack_num)
            assert s.peek(stack_num) == i
            assert not s.is_empty(stack_num)
            assert not s.is_full(stack_num)

        s.push(999, stack_num=stack_num)
        with pytest.raises(StackFullError):
            s.push(777, stack_num=stack_num)

        assert not s.is_empty(stack_num)
        assert s.is_full(stack_num)

        assert s.peek(stack_num) == 999
        assert s.pop(stack_num) == 999
        assert not s.is_empty(stack_num)
        assert not s.is_full(stack_num)

        for i in range(stack_size - 2, 0, -1):
            assert s.peek(stack_num) == i
            assert s.pop(stack_num) == i
            assert not s.is_empty(stack_num)
            assert not s.is_full(stack_num)

        assert s.peek(stack_num) == 0
        assert s.pop(stack_num) == 0
        assert s.is_empty(stack_num)
        assert not s.is_full(stack_num)

        with pytest.raises(StackEmptyError):
            s.peek(stack_num)
        with pytest.raises(StackEmptyError):
            s.pop(stack_num)


def test_stack_does_not_exist():
    s = MultiStack(stack_size=3, number_of_stacks=1)
    with pytest.raises(StackDoesNotExistError):
        s.push(1, 1)


if __name__ == "__main__":
    newstack = MultiStack(2, 2)
    print(newstack.is_empty(1))
    newstack.push(3, 1)
    print(newstack.peek(1))
    print(newstack.is_empty(1))
    newstack.push(2, 1)
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    newstack.push(3, 1)
