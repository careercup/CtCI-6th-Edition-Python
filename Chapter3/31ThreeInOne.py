class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


def ThreeInOne():
    newstack = MultiStack(2)
    print newstack.IsEmpty(1)
    newstack.Push(3, 1)
    print newstack.Peek(1)
    print newstack.IsEmpty(1)
    newstack.Push(2, 1)
    print newstack.Peek(1)
    print newstack.Pop(1)
    print newstack.Peek(1)
    newstack.Push(3, 1)

ThreeInOne()


#IMPLEMENTATION FOR K STACKS 
# Python 3 program to demonstrate implementation 
# of k stacks in a single array in time and space 
# efficient way 
class KStacks: 
	
	def __init__(self, k, n): 
		self.k = k # Number of stacks. 
		self.n = n # Total size of array holding 
				# all the 'k' stacks. 

		# Array which holds 'k' stacks. 
		self.arr = [0] * self.n 

		# All stacks are empty to begin with 
		# (-1 denotes stack is empty). 
		self.top = [-1] * self.k 

		# Top of the free stack. 
		self.free = 0

		# Points to the next element in either 
		# 1. One of the 'k' stacks or, 
		# 2. The 'free' stack. 
		self.next = [i + 1 for i in range(self.n)] 
		self.next[self.n - 1] = -1

	# Check whether given stack is empty. 
	def isEmpty(self, sn): 
		return self.top[sn] == -1

	# Check whether there is space left for 
	# pushing new elements or not. 
	def isFull(self): 
		return self.free == -1

	# Push 'item' onto given stack number 'sn'. 
	def push(self, item, sn): 
		if self.isFull(): 
			print("Stack Overflow") 
			return

		# Get the first free position 
		# to insert at. 
		insert_at = self.free 

		# Adjust the free position. 
		self.free = self.next[self.free] 

		# Insert the item at the free 
		# position we obtained above. 
		self.arr[insert_at] = item 

		# Adjust next to point to the old 
		# top of stack element. 
		self.next[insert_at] = self.top[sn] 

		# Set the new top of the stack. 
		self.top[sn] = insert_at 

	# Pop item from given stack number 'sn'. 
	def pop(self, sn): 
		if self.isEmpty(sn): 
			return None

		# Get the item at the top of the stack. 
		top_of_stack = self.top[sn] 

		# Set new top of stack. 
		self.top[sn] = self.next[self.top[sn]] 

		# Push the old top_of_stack to 
		# the 'free' stack. 
		self.next[top_of_stack] = self.free 
		self.free = top_of_stack 

		return self.arr[top_of_stack] 

	def printstack(self, sn): 
		top_index = self.top[sn] 
		while (top_index != -1): 
			print(self.arr[top_index]) 
			top_index = self.next[top_index] 

# Driver Code 
if __name__ == "__main__": 
	
	# Create 3 stacks using an 
	# array of size 10. 
	kstacks = KStacks(3, 10) 

	# Push some items onto stack number 2. 
	kstacks.push(15, 2) 
	kstacks.push(45, 2) 

	# Push some items onto stack number 1. 
	kstacks.push(17, 1) 
	kstacks.push(49, 1) 
	kstacks.push(39, 1) 

	# Push some items onto stack number 0. 
	kstacks.push(11, 0) 
	kstacks.push(9, 0) 
	kstacks.push(7, 0) 

	print("Popped element from stack 2 is " +
						str(kstacks.pop(2))) 
	print("Popped element from stack 1 is " +
						str(kstacks.pop(1))) 
	print("Popped element from stack 0 is " +
						str(kstacks.pop(0))) 

	kstacks.printstack(0) 
