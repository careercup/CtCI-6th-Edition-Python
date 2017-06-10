

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15,16,  18, 22, 43, 144, 515, 4123]
s_list =testArray

class tree_build:
	def __init__(self, l_list):
		self.in_list = l_list
	def binary_tree(self, list_of_nodes):
		end = len(list_of_nodes)
		root = int(((end) / 2))
		middle = list_of_nodes[root]
		left = list_of_nodes[:(root-1)]
		right = list_of_nodes[root:]
		if len(right) > 1:
			right = self.binary_tree(right)
		if len(left) > 1:
			left = self.binary_tree(left)
		output = (left, ':L', middle, 'R:', right)

		return output
	def tree(self):
		list_of_nodes = self.in_list
		result = self.binary_tree(list_of_nodes)
		return result

	
x = tree_build(testArray)

x.tree()

