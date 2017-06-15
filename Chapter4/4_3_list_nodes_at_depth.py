
"""these are the 4.2 answer, used to make the input for list_of_levels """
from binary_tree_build_42 import Node, tree_build

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15,16, 18, 22, 43, 144, 515, 4123]

x = tree_build(testArray)

print(x.root)



class list_of_levels(tree_root):
	def __init__(tree_root):
		self.list_levels = [[]]
		depth = 0
		add_to_levels(self,tree_root, depth)

	def add_to_levels(self, position, depth):
		if depth > len(self.list_levels):
			self.list_levels.append(position.node)
		else:
			self.list_levels[depth].append(position.node)
		if position.left != 0:
			add_to_levels(position.left,depth+=1)
		if position.right !=0:
			add_to_levels(position.right,depth+=1)
