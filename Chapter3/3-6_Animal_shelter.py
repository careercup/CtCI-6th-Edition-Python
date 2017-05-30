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
#with dogs in queue1 and cats in queue1
#enter a 2 if you wish for any old species to be returned

class animalshelter(stack):
    def __init__(self):
        self.queuecat = queue()
        self.queuedogs = queue()
        self.queuetotal = queue()
        self.array = [self.queuecat, self.queuedogs, self.queuetotal]
    def add(self, position, value):
        self.array[position].add(value)
        self.array.queuetotal.add((position, value))
    def pop(self, position):
        if position == 2:
        	output = self.queuetotal(pop)
        	if output[0] == 0:
        		self.queuecat.pop()
        	elif output[0] == 1:
        		self.queuedog.pop()
        	return output[1]
        return self.array[position].pop()
    def peek(self, position):
        return self.array[position].peek()
    def isEmpty(self,position):
        return self.array[position].isEmpty()


