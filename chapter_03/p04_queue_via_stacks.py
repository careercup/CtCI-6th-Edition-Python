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
    def test_peek(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)

    def test_add(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)
        q.add(101)
        self.assertNotEqual(q.peek(), 101)

    def test_remove(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.remove(), 4)
        self.assertEqual(q.remove(), 6)
        self.assertEqual(len(q), 0)
        self.assertFalse(q.remove())
