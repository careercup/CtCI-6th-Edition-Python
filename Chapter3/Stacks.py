
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return True if len(self.stack) == 0 else False


