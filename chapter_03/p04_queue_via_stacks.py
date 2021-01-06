# 3.4 Queue Via Stacks
import unittest

from chapter_03.stack import Stack


class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def _shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def add(self, value):
        return self.new_stack.push(value)

    def peek(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.peek()

    def remove(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.pop()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.new_stack) + len(self.old_stack)


class Tests(unittest.TestCase):
    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def test_shift_stacks(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert len(q.old_stack) == 0
            assert len(q.new_stack) == len(sequence)
            assert q.new_stack.peek() == sequence[-1]
            q._shift_stacks()
            assert len(q.old_stack) == len(sequence)
            assert len(q.new_stack) == 0
            assert q.old_stack.peek() == sequence[0]

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                assert q.peek() == sequence[0]
            q.remove()
            assert q.peek() == sequence[1]

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()
