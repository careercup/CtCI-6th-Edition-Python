"""Given a binary tree, create a linked list which holds all nodes at a given depth."""

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
        self.level = None


class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.root.level = 0
        self.levels = {}

    def create_list(self):
        # BFS.
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node = q.popleft()
            if node.level not in self.levels:
                # First node in the level
                self.levels[node.level] = LinkedNode(node.name)
            else:
                # Nodes already exist
                last = self.levels[node.level].get_last()
                last.next = LinkedNode(node.name)
            # Push onto queue
            if node.left:
                node.left.level = node.level + 1
                q.append(node.left)
            if node.right:
                node.right.level = node.level + 1
                q.append(node.right)

if __name__ == "__main__":
    root = BinaryNode(0)
    t = BinaryTree(root)
    t.root.left = BinaryNode(1)
    t.root.right = BinaryNode(2)
    t.root.left.left = BinaryNode(3)
    t.root.left.right = BinaryNode(4)
    t.root.right.left = BinaryNode(5)
    t.root.right.right = BinaryNode(6)
    t.create_list()
    print(t.levels)
