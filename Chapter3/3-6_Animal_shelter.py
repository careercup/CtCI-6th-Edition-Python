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


#to simulate the animal shelter, use the this multi queue class, 
#with dogs in queue0 and cats in queue1

class multiqueues(stack):
    def __init__(self):
        self.queue0 = queue()
        self.queue1 = queue()
        self.array = [self.queue1, self.queue2]
    def add(self, position, value):
        self.array[position].add(value)
    def pop(self, position):
        return self.array[position].pop()
    def peek(self, position):
        return self.array[position].peek()
    def isEmpty(self,position):
        return self.array[position].isEmpty()


