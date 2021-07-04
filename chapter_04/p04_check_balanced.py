class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Version 2:
# Traverse the tree and track the largest and smallest depth of each leaf node.
# Then compare the largest and smallest depth.
def is_balanced_v2(node):
    min_depth = 10 ** 100
    max_depth = -(10 ** 100)
    queue = [(node, 0)]
    visited = [node]

    while len(queue) > 0:
        curr_node, curr_depth = queue.pop(0)

        if curr_node.left is None and curr_node.right is None:
            if curr_depth > max_depth:
                maxDepth = curr_depth
            if curr_depth < min_depth:
                min_depth = curr_depth
        else:
            if curr_node.left and curr_node.left not in visited:
                visited.append(curr_node.left)
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right and curr_node.right not in visited:
                visited.append(curr_node.right)
                queue.append((curr_node.right, curr_depth + 1))

    return maxDepth - min_depth < 2


def find_max_depth(node, level=0):
    if node is None:
        return level
    if not node.left:
        return find_max_depth(node.right, level + 1)
    if not node.right:
        return find_max_depth(node.left, level + 1)
    return max(
        find_max_depth(node.left, level + 1), find_max_depth(node.right, level + 1)
    )


def find_min_depth(node, level=0):
    if node is None:
        return level
    if not node.left:
        return find_min_depth(node.right, level + 1)
    if not node.right:
        return find_min_depth(node.left, level + 1)
    return min(
        find_min_depth(node.left, level + 1), find_min_depth(node.right, level + 1)
    )


# Version 1:
# Find the max tree depth and min tree depth independently.
# Then compare their values.
def is_balanced_v1(node):
    return find_max_depth(node) - find_min_depth(node) < 2


def example():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    assert is_balanced_v1(root) == is_balanced_v2(root) is True

    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    assert is_balanced_v1(root) == is_balanced_v2(root) is False

    tree = BinaryNode(1)
    tree.left = BinaryNode(2)
    tree.right = BinaryNode(9)
    tree.right.left = BinaryNode(10)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(7)
    tree.left.right.right = BinaryNode(5)
    tree.left.left.left = BinaryNode(6)
    tree.left.right.left = BinaryNode(12)
    tree.left.right.left.left = BinaryNode(16)
    tree.left.right.left.right = BinaryNode(0)
    assert is_balanced_v1(tree) == is_balanced_v2(tree) is False

    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    assert is_balanced_v1(root) == is_balanced_v2(root) is True


if __name__ == "__main__":
    example()
