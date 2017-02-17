""" Check if a binary tree is balanced, i.e. heights of subtrees differ by <= 1.
"""

class BinaryNode:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def is_balanced(self, node=None):
        if node is None:
            node = self.root

        if node.left and node.right:
            return self.is_balanced(node.left) and self.is_balanced(node.right)

        if node.left:  # but not node.right
            if node.left.left or node.left.right:
                return False  # two layers, unbalanced

        if node.right:
            if node.right.left or node.right.right:
                return False

        return True

if __name__ == "__main__":
    bt = BinaryTree(BinaryNode(1))
    bt.root.left = BinaryNode(2)
    bt.root.left.left = BinaryNode(4)
    bt.root.left.right = BinaryNode(5)
    bt.root.left.right.right = BinaryNode(6)
    bt.root.left.right.right.right = BinaryNode(7)
    bt.root.right = BinaryNode(3)
    bt.root.right.left = BinaryNode(8)
    bt.root.right.right = BinaryNode(9)
    bt.root.right.right.right = BinaryNode(10)
    bt.root.right.right.right.right = BinaryNode(11)
    print(bt.is_balanced())
