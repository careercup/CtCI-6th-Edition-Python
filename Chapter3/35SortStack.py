from Stack import Stack

def sort(stack):
    tmp = Stack()
    tmp.push(stack.pop())
    while not stack.is_empty():
        top = stack.pop()    
        while tmp.peek() and top < tmp.peek():
            stack.push(tmp.pop())
        tmp.push(top)
    while not tmp.is_empty():
        stack.push(tmp.pop())


stack = Stack()
stack.push(7)
stack.push(10)
stack.push(5)
stack.push(3)
stack.push(1)
stack.push(12)
stack.push(8)
print(stack)
sort(stack)
print(stack)
