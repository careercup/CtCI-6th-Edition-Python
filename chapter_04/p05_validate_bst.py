from chapter_04.binary_search_tree import BinarySearchTree
from chapter_04.binary_tree import BinaryTree


def is_binary_search_tree(tree):
    return _is_bst(tree.root)


def _is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    if (min_val and node.key < min_val) or (max_val and node.key >= max_val):
        return False
    return _is_bst(node.left, min_val, node.key) and _is_bst(
        node.right, node.key, max_val
    )


def test_is_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    t = BinaryTree()
    n1 = t.insert(5, None)
    n2 = t.insert(4, n1)
    n3 = t.insert(6, n1)
    n4 = t.insert(3, n2)
    t.insert(6, n2)
    t.insert(5, n3)
    t.insert(2, n4)

    assert not is_binary_search_tree(t)
    assert is_binary_search_tree(bst)
