class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+'Left :'+str(self.left) + "  Value : " + str(self.val) + "  Right :" + str(self.right)+')'

# ----------------------Function for the solution-----------------------------------------


def check_balanced(root):
    if check_balanced_helper(root) == -1:
        return 'NO'
    return 'YES'


def check_balanced_helper(root):
    if root is None:                           # Base case
        return 0

    left_height = check_balanced_helper(root.left)   # Checking height at left side of the Node
    if left_height == -1:
        return -1
    right_height = check_balanced_helper(root.right)  # Checking height at right side of the Node
    if right_height == -1:
        return -1

    if left_height - right_height > 1:
        return -1

    return max(left_height, right_height) + 1          # Returning actual height of the subtree

# ----------------------------------------------------------------------------------------


def initiate_array_to_binary(array):
    return array_to_binary(array, 0, len(array) - 1)


def array_to_binary(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = array_to_binary(array, start, mid - 1)
    root.right = array_to_binary(array, mid + 1, end)
    return root


testArray = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
Binary_Tree = initiate_array_to_binary(testArray)
print('Binary Tree: ', str(Binary_Tree))

print('\nIs the Binary Tree balanced ? :', check_balanced(Binary_Tree))


