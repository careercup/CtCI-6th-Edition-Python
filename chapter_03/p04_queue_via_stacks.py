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
        for vals in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(vals, start=1):
                q.add(val)
                self.assertEqual(len(q), index)
            for index, val in enumerate(vals, start=1):
                q.remove()
                self.assertEqual(len(q), len(vals) - index)

    def test_add(self):
        for vals in self.test_cases:
            q = MyQueue()
            for val in vals:
                q.add(val)
            self.assertEqual(q.peek(), vals[0])
            self.assertEqual(len(q), len(vals))

    def test_shift_stacks(self):
        for vals in self.test_cases:
            q = MyQueue()
            for val in vals:
                q.add(val)
            self.assertEqual(len(q.old_stack), 0)
            self.assertEqual(len(q.new_stack), len(vals))
            self.assertEqual(q.new_stack.peek(), vals[-1])
            q._shift_stacks()
            self.assertEqual(len(q.old_stack), len(vals))
            self.assertEqual(len(q.new_stack), 0)
            self.assertEqual(q.old_stack.peek(), vals[0])

    def test_peek(self):
        for vals in self.test_cases:
            q = MyQueue()
            for val in vals:
                q.add(val)
                self.assertEqual(q.peek(), vals[0])
            q.remove()
            self.assertEqual(q.peek(), vals[1])

    def test_remove(self):
        for vals in self.test_cases:
            q = MyQueue()
            for val in vals:
                q.add(val)
            for i in range(len(vals)):
                self.assertEqual(q.remove(), vals[i])

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)
        q.add(101)
        self.assertNotEqual(q.peek(), 101)

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.remove(), 4)
        self.assertEqual(q.remove(), 6)
        self.assertEqual(len(q), 0)
        self.assertFalse(q.remove())
