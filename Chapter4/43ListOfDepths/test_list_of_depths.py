from list_of_depths import *


class TreeNode(object):
    def __init__(self, value=None):
        self.head = value
        self.left = None
        self.right = None


def array_to_btree(arr):

    tree = TreeNode()
    if len(arr) == 0:
        return tree

    median = len(arr)//2
    left = arr[:median]
    right = arr[median+1:]
    if len(left) > 0:
        tree.left = array_to_btree(left)
    tree.head = TreeNode(arr[median])
    if len(right) > 0:
        tree.right = array_to_btree(right)
    return tree


def linked_list_to_array(t_list, arr=[]):
    if t_list.head.value is not None:
        return __linked_list_to_array_helper__(t_list, arr=[])
    else:
        return []


def __linked_list_to_array_helper__(t_list, arr=[]):
    if len(arr) == 0:
        arr.append(t_list.head.value)
        __linked_list_to_array_helper__(t_list.head.next, arr)
    elif t_list != None:
        arr.append(t_list.value)
        __linked_list_to_array_helper__(t_list.next, arr)
    return arr


def test_list_of_depths():
    test_cases = {
        0: [1, 2, 3],
        1: [1, 2, 3, 4, 5, 6, 7],
        3: [],
        4: [5, 5, 5],
        5: ['this', 'is', 'WoRkInG']
    }
    results = {}
    for k, v in test_cases.items():
        tree = array_to_btree(v)
        tree_linked_list = list_of_depths(tree)
        results[k] = linked_list_to_array(tree_linked_list, [])

    assert results == test_cases


test_list_of_depths()
