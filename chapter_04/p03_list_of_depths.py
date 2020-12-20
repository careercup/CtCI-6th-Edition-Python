from collections import deque


class LinkedNode:
    def __init__(self, name):
        self.name = name
        self.next = None

    def get_last(self):
        node = self
        while node.next:
            node = node.next
        return node

    def __repr__(self):
        rv = []
        node = self
        while node:
            rv.append(node.name)
            node = node.next
        return str(rv)


class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def create_node_list_by_depth(tree_root):
    # BFS.
    levels = {}
    q = deque()
    q.append((tree_root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            # First node in the level
            levels[level] = LinkedNode(node.name)
        else:
            # Nodes already exist
            last = levels[level].get_last()
            last.next = LinkedNode(node.name)
        # Push onto queue
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels


def test_create_node_list_by_depth():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    assert repr(levels) == repr({0: [0], 1: [1, 2], 2: [3, 4, 5, 6]})


if __name__ == "__main__":
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    print(levels)
