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
        self.assertEqual(q.remove(), 4)
        self.assertEqual(q.remove(), 6)

        self.assertFalse(q.remove())

    def test_enqueue_one(self):
        queue = MyQueue()
        assert queue.is_empty()
        queue.add(1)
        assert not queue.is_empty()
        self.assertEqual(len(queue), 1)

    def test_enqueue_two(self):
        queue = MyQueue()
        queue.add(1)
        queue.add(2)
        self.assertEqual(len(queue), 2)

    def test_enqueue_three(self):
        queue = MyQueue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        self.assertEqual(len(queue), 3)

    def test_dequeue_one(self):
        queue = MyQueue()
        queue.add(1)
        self.assertEqual(queue.remove(), 1)

    def test_dequeue_two(self):
        queue = MyQueue()
        queue.add(1)
        queue.add(2)
        self.assertEqual(queue.remove(), 1)
        self.assertEqual(queue.remove(), 2)

    def test_dequeue_three(self):
        queue = MyQueue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        self.assertEqual(queue.remove(), 1)
        self.assertEqual(queue.remove(), 2)
        self.assertEqual(queue.remove(), 3)
