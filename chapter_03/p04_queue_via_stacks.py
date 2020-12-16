# 3.4 Queue Via Stacks
import unittest

from chapter_03.stack import Stack


class MyQueue:
    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def enqueue(self, item):
        while not self.a.is_empty():
            self.b.push(self.a.pop())
        self.b.push(item)

        while not self.b.is_empty():
            self.a.push(self.b.pop())

    def dequeue(self):
        if not self.a.is_empty():
            return self.a.pop()
        else:
            if not self.b.is_empty():
                return self.b.pop()
            return None

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.a) + len(self.b)


class Tests(unittest.TestCase):
    def test_enqueue_one(self):
        queue = MyQueue()
        assert queue.is_empty()
        queue.enqueue(1)
        assert not queue.is_empty()
        self.assertEqual(len(queue), 1)

    def test_enqueue_two(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(len(queue), 2)

    def test_enqueue_three(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(len(queue), 3)

    def test_dequeue_one(self):
        queue = MyQueue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)

    def test_dequeue_two(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_dequeue_three(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
