class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]
        return None

    def __len__(self):
        # in python the `len` function is preferred to `size` methods
        return len(self.items)

    def __bool__(self):
        # lets us use the stack as a conditional
        return bool(self.items)
