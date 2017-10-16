class stack:
	def __init__(self):
		self.items = []

	def pop(self):		
		return self.items.pop()

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[len(self.items) - 1]

	def isEmpty(self):
		return len(self.items) == 0


class MyQueue:
	def __init__(self):
		self.push_stack = stack()
		self.remove_stack = stack()

	def shiftStacks(self, s1, s2):
		while not s2.isEmpty():
			s1.push(s2.pop())

	def push(self, item):
		if self.push_stack.isEmpty():
			self.shiftStacks(self.push_stack, self.remove_stack)
		self.push_stack.push(item)

	def remove(self):
		if self.remove_stack.isEmpty():
			self.shiftStacks(self.remove_stack, self.push_stack)
		return self.remove_stack.pop()

	def peek(self):
		if self.remove_stack.isEmpty():
			self.shiftStacks(self.remove_stack, self.push_stack)
		return self.remove_stack.peek()

	def isEmpty(self):
		return self.push_stack.isEmpty() and self.remove_stack.isEmpty()

q = MyQueue()

print q.isEmpty()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print q.remove()
print q.remove()
print q.peek()
print q.isEmpty()
