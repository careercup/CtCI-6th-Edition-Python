# 3.4: Queue via Stacks
import random
import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def peek(self):
        if not self.top:
            return None
        return self.top.value


class MyQueue:
    def __init__(self, capacity=None):
        self.capacity = capacity // 2 if capacity else 5
        self.new_stack = Stack(self.capacity)
        self.old_stack = Stack(self.capacity)

    def _shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def size(self):
        return self.new_stack.size + self.old_stack.size

    def is_empty(self):
        return self.new_stack.is_empty() and self.old_stack.is_empty()

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


class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.q = MyQueue()

        self.values = [random.randint(10, 100) for _ in range(self.q.capacity)]
        for v in self.values:
            self.q.add(v)

    def test_peek(self):
        self.assertEqual(self.q.peek(), self.values[0])

    def test_add(self):
        self.assertEqual(self.q.peek(), self.values[0])
        self.q.add(101)
        self.assertNotEqual(self.q.peek(), 101)

    def test_remove(self):
        for v in self.values:
            self.assertEqual(self.q.remove(), v)

        self.assertFalse(self.q.remove())


if __name__ == '__main__':
    unittest.main()
