class Node(object):
    """Singly Node for Linked List data structure
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """Singly Linked List data structure
    """

    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        """Append a node at the end
        """
        if self.head.value is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self


def list_of_depths(tree, linked_list=None):
    """Turns tree structure to linked list using DFS recursion algorithm

    Arguments:
        tree {tree} -- tree data structure 

    Keyword Arguments:
        linked_list {linked list} -- (default: {None})

    Returns:
        linked list -- linked list that has these tree values
    """

    if linked_list == None:
        linked_list = LinkedList(None)

    # Edge cases
    if tree.head is None:
        return linked_list

    if tree.left != None:
        list_of_depths(tree.left, linked_list)
    linked_list.append(tree.head.head)
    if tree.right != None:
        list_of_depths(tree.right, linked_list)

    return linked_list


if __name__ == "__main__":
    pass
