#3.5 Sort Stacks
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
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        return None

    def size(self):
        return len(self.items)


class SortedStack:
    def __init__(self):
        self.stack = Stack()
        self.temp_stack = Stack()

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        if self.stack.is_empty() or item < self.stack.peek():
            self.stack.push(item)
        else:
            while self.stack.peek() is not None and item > self.stack.peek():
                self.temp_stack.push(self.stack.pop())
            self.stack.push(item)
            while not self.temp_stack.is_empty():
                self.stack.push(self.temp_stack.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]
        return None

    def size(self):
        return self.stack.size()


class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        self.assertEquals(queue.size(), 1)

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        self.assertEquals(queue.size(), 2)

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        self.assertEquals(queue.size(), 3)

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        self.assertEquals(queue.pop(), 1)

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        self.assertEquals(queue.pop(), 1)
        self.assertEquals(queue.pop(), 2)

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        self.assertEquals(queue.pop(), 1)
        self.assertEquals(queue.pop(), 2)
        self.assertEquals(queue.pop(), 3)

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        self.assertEquals(queue.pop(), 1)
        self.assertEquals(queue.pop(), 2)
        self.assertEquals(queue.pop(), 3)
        self.assertEquals(queue.pop(), 4)