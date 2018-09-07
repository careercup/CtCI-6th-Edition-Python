class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+'Left :'+str(self.left) + "  Value : " + str(self.val) + "  Right :" + str(self.right)+')'

# ----------------------Function for the solution-----------------------------------------


def list_of_depths(root):

    result = []         # list containing list of Nodes of each level
    current = []        # list representing the Nodes present for a particular level

    # Visiting the root Node
    if root is not None:
        current.append(root)

    while len(current):
        result.append([i.val for i in current])        # Adding the list of value of Nodes of a level (previous one)
        parents = current                              # List which will be containing value of Nodes of the next level
        current = []

        for parent in parents:
            # Visiting the children
            if parent.left is not None:
                current.append(parent.left)
            if parent.right is not None:
                current.append(parent.right)

    return result

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

print('\nList of all the Nodes at each level :')

result = list_of_depths(Binary_Tree)

for i in result:
    print(i)
    print('')



