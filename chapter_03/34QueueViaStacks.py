# 3.4 Queue Via Stacks
import unittest


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


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
        return not self.a.is_empty() or not self.b.is_empty()

    def size(self):
        return self.a.size() + self.b.size()


class Tests(unittest.TestCase):
    def test_enqueue_one(self):
        queue = MyQueue()
        queue.enqueue(1)
        self.assertEquals(queue.size(), 1)

    def test_enqueue_two(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEquals(queue.size(), 2)

    def test_enqueue_three(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEquals(queue.size(), 3)

    def test_dequeue_one(self):
        queue = MyQueue()
        queue.enqueue(1)
        self.assertEquals(queue.dequeue(), 1)

    def test_dequeue_two(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEquals(queue.dequeue(), 1)
        self.assertEquals(queue.dequeue(), 2)

    def test_dequeue_three(self):
        queue = MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEquals(queue.dequeue(), 1)
        self.assertEquals(queue.dequeue(), 2)
        self.assertEquals(queue.dequeue(), 3)
