
f.right = right

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15,16, 18, 22, 43, 144, 515, 4123]
s_list =testArray

class tree_build:
	def __init__(self, l_list):
		self.in_list = l_list
	def binary_tree(self, list_of_nodes):
		root = int((len(list_of_nodes) // 2))
		middle = list_of_nodes[root]
		left = list_of_nodes[:(root-1)]
		right = list_of_nodes[root+1:]
		if len(right) > 1:
			right = self.binary_tree(right)
		if len(left) > 1:
			left = self.binary_tree(left)
		output = (left, ':L', middle, 'R:', right)
		""" trim the dead ends"""
		if (len(right) == 0)  or (str(right) == middle):
			output = output[:-2]
		if len(left) == 0 or (left == middle):
			output = output[2:]
		return output
	def tree(self):
		list_of_nodes = self.in_list
		result = self.binary_tree(list_of_nodes)
		return result

	
x = tree_build(testArray)

x.tree()


#alternative version, builds an object that can be stepped through using .node
# .left and .right is this more what is being asked for?
class Node:
	def __init__(self, middle):
		self.node =  middle
		self.left = 0
		self.right = 0
	def add_left(self, left):
		self.left = left
	def add_right(self, right):
		self.right = right
	def __str__(self):
		return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'



""" below variant you can walk through"""
class tree_build:
	def __init__(self, l_list):
		self.in_list = l_list
	def binary_tree(self, list_of_nodes,call_no):
		root = int((len(list_of_nodes) // 2))
		middle = list_of_nodes[root]
		left = list_of_nodes[:(root-1)]
		right = list_of_nodes[root+1:]
		node = Node(middle)
		if call_no == 0:
			self.root = node
			call_no += 1
		if len(right) > 1:
			right = self.binary_tree(right,call_no)
			node.add_right(right)
		if len(left) > 1:
			left = self.binary_tree(left,call_no)
			node.add_left(left)
		output = (left, ':L', middle, 'R:', right)
		""" trim the dead ends"""
		if (len(right) == 0)  or (str(right) == middle):
			output = output[:-2]
		if len(left) == 0 or (left == middle):
			output = output[2:]
		return output
	def tree(self):
		list_of_nodes = self.in_list
		result = self.binary_tree(list_of_nodes,0)
		return result


x = tree_build(testArray)

print(x.tree())
