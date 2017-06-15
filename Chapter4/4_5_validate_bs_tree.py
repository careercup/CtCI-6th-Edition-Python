from binary_tree_build_42 import Node, tree_build

def search_tree_check(root):
	if root.right > root.node:
		search_tree_check(root.right)
	if root.left <= root.node:
		search_tree_check(root.right)
	if (root.right == 0) and (root.left == 0):
		return True