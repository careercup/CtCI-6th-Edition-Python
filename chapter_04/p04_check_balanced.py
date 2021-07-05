class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# Version 2: 
# Traverse the tree and track the largest and smallest depth of each leaf node.
# Then compare the largest and smallest depth.
def is_balanced_v2(node):
    minDepth = 10 ** 100
    maxDepth = -10 ** 100
    queue = [(node, 0)]
    visited = [node]

    while len(queue) > 0:
        currNode, currDepth = queue.pop(0)

        if currNode.left is None and currNode.right is None:
            if currDepth > maxDepth:
                maxDepth = currDepth
            if currDepth < minDepth:
                minDepth = currDepth
        else:
            if currNode.left and currNode.left not in visited:
                visited.append(currNode.left)
                queue.append((currNode.left, currDepth + 1))
            if currNode.right and currNode.right not in visited:
                visited.append(currNode.right)
                queue.append((currNode.right, currDepth + 1))

    return maxDepth - minDepth < 2
        

def findMaxDepth(node, level = 0):
    if node is None:
        return level
    if not node.left:
        return findMaxDepth(node.right, level + 1)
    if not node.right:
        return findMaxDepth(node.left, level + 1)
    return max(findMaxDepth(node.left, level + 1), findMaxDepth(node.right, level + 1))

def findMinDepth(node, level = 0):
    if node is None:
        return level
    if not node.left:
        return findMinDepth(node.right, level + 1)
    if not node.right:
        return findMinDepth(node.left, level + 1)
    return min(findMinDepth(node.left, level + 1), findMinDepth(node.right, level + 1))

# Version 1:
# Find the max tree depth and min tree depth independently.
# Then compare their values.
def is_balanced_v1(node):
    return findMaxDepth(node) - findMinDepth(node) < 2

def example():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    assert is_balanced_v1(root) == is_balanced_v2(root) == True

    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    assert is_balanced_v1(root) == is_balanced_v2(root) == False

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
    assert is_balanced_v1(tree) == is_balanced_v2(tree) == False

    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    assert is_balanced_v1(root) == is_balanced_v2(root) == True


if __name__ == "__main__":
    example()
