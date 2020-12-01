import unittest


class MyQueue():
    """
    Implements a queue (with expected size, add, peek, and remove 
    methods) using two stacks. One stack will hold new elements, the 
    other stack will hold oldest elements. Elements added to queue are 
    pushed to stack of new elements, elements removed from queue are 
    popped from stack of oldest elements.

    stack_class : Class
        Implementation of a Stack
    stack_size : int, optional
        The optional max-size of each stack
    """

    def __init__(self, stack_class, stack_size=None):
        self.stack_newest = stack_class(stack_size)
        self.stack_oldest = stack_class(stack_size)

    def size(self):
        return self.stack_newest.size() + self.stack_oldest.size()

    def add(self, val):
        self.stack_newest.push(val)

    def shift_stacks(self):
        """
        Move elements from new stack to old stack so we can perform 
        operations such as peek or remove
        """
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest.peek()

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()


class TestMyQueue(unittest.TestCase):

    #Declare your stack class here
    stack_class = Stack

    test_cases = [
        ([1, 2, 3]),
        ([-1, 0, 1]),
        (["a", "b", "c", "d", "e", "f"])
    ]

    def test_size(self):
        for vals in self.test_cases:
            q = MyQueue(self.stack_class)
            for index, val in enumerate(vals, start=1):
                q.add(val)
                self.assertEqual(q.size(), index)
            for index, val in enumerate(vals, start=1):
                q.remove()
                self.assertEqual(q.size(), len(vals) - index)

    def test_add(self):
        for vals in self.test_cases:
            q = MyQueue(self.stack_class)
            for val in vals:
                q.add(val)
            self.assertEqual(q.peek(), vals[0])
            self.assertEqual(q.size(), len(vals))

    def test_shift_stacks(self):
        for vals in self.test_cases:
            q = MyQueue(self.stack_class)
            for val in vals:
                q.add(val)
            self.assertEqual(q.stack_oldest.size(), 0)
            self.assertEqual(q.stack_newest.size(), len(vals))
            self.assertEqual(q.stack_newest.peek(), vals[-1])
            q.shift_stacks()
            self.assertEqual(q.stack_oldest.size(), len(vals))
            self.assertEqual(q.stack_newest.size(), 0)
            self.assertEqual(q.stack_oldest.peek(), vals[0])

    def test_peek(self):
        for vals in self.test_cases:
            q = MyQueue(self.stack_class)
            for val in vals:
                q.add(val)
                self.assertEqual(q.peek(), vals[0])
            q.remove()
            self.assertEqual(q.peek(), vals[1])

    def test_remove(self):
        for vals in self.test_cases:
            q = MyQueue(self.stack_class)
            for val in vals:
                q.add(val)
            for i in range(len(vals)):
                self.assertEqual(q.remove(), vals[i])


if __name__ == "__main__":
    unittest.main()
