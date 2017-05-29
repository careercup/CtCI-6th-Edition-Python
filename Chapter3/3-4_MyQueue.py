
#3.4 build class MyQueue using two stacks
#for way described in book:
class MyQueue(stack):
    def __init__(self):
        self.stack_in = stack()
        self.stack_temp = stack()
    def add(self, list_or_obj):
        self.stack_in.add(list_ot_obj)
    def remove(self):
        while self.stack_in.isEmpty() == False:
            self.stack_temp.add(self.stack_in.pop())
        front = self.stack_temp.pop()
        while self.stack_temp.isEmpty() == False:
            self.stack_in.add(self.stack_temp.pop())
        return front
    def peek(self):
        while self.stack_in.isEmpty() == False:
            self.stack_temp.add(self.stack_in.pop())
        front = self.stack_temp.peek()
        while self.stack_temp.isEmpty() == False:
            self.stack_in.add(self.stack_temp.pop())
        return front
    def isEmpty(self):
        return self.stack_in.isEmpty()


#alternative, using a modified stack instead of two stacks


class queue:
    def __init__(self):
        self.queue = []
    
    def add(self, list_or_obj):
        if type(list_or_obj) == list:
            self.queue.extend(list_or_obj)
        else:
            self.queue.append(list_or_obj)

    def pop(self):
        first_in_line = self.queue[0]
        self.queue = self.queue[0:]
        return first_in_line

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def min(self):
        return min(self.queue)

