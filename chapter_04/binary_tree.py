class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new = self.NodeCls(key)
        if parent is None:
            if self.root is None:
                self.root = new
                return new
            raise Exception("a root already exists")

        if not parent.left:
            parent.left = new
            new.parent = parent
        elif not parent.right:
            parent.right = new
            new.parent = parent
        else:
            raise Exception("a node cannot have more than two children")
        return new


def example():
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    t.insert(5, n2)
    t.insert(7, n3)
    t.insert(8, n4)

    print(t.root.left.left.left.key)


if __name__ == "__main__":
    example()
