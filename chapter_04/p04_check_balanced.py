class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def is_balanced(node):

    if node.left and node.right:
        return is_balanced(node.left) and is_balanced(node.right)

    if node.left:  # but not node.right
        if node.left.left or node.left.right:
            return False  # two layers, unbalanced

    if node.right:
        if node.right.left or node.right.right:
            return False

    return True


def test_is_balanced():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    assert is_balanced(root)
    root.left.left = BinaryNode(4)
    assert not is_balanced(root)


def example():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    print(is_balanced(root))
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    print(is_balanced(root))


if __name__ == "__main__":
    example()
