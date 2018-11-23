class LinkedListNode:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Stack:
    
    def __init__(self,values=None):
        self.top = None
        if values!=None:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self.top
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def push(self, value):
        new = LinkedListNode(value)
        new.next = self.top
        self.top = new
        
    def pop(self):
        if self.top == None:
            return
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.top == None: return None
        return self.top.value
