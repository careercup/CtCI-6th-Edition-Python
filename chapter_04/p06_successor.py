from chapter_04.binary_search_tree import BinarySearchTree


def in_order_successor(input_node):
    if input_node is None:
        return None
    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current
    else:
        ancestor = input_node.parent
        child = input_node
        while ancestor and ancestor.right == child:
            child = ancestor
            ancestor = ancestor.parent
        return ancestor


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Get a reference to the node whose key is 9
    test = bst.get_node(12)

    # Find the in order successor of test
    succ = in_order_successor(test)

    # Print the key of the successor node
    if succ is not None:
        print("\nInorder Successor of %d is %d " % (test.key, succ.key))
    else:
        print("\nInorder Successor doesn't exist")
