class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item


def inorder(root):
    if root:
        inorder(root.left)
        print root.val
        inorder(root.right)


def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)


def arrayToBinary(array, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    root = Node(array[mid])
    root.left = arrayToBinary(array, start, mid - 1)
    root.right = arrayToBinary(array, mid + 1, end)
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
r = initiateArrayToBinary(testArray)
inorder(r)
