from chapter_04.binary_tree import BinaryTree, Node


def first_common_ancestor(p: Node, q: Node):
    if not p or not q:
        return None
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    delta = abs(depth_p - depth_q)
    if depth_p < depth_q:
        for _ in range(delta):
            q = q.parent
    elif depth_q < depth_p:
        for _ in range(delta):
            p = p.parent
    ancestor_p = p
    ancestor_q = q
    while ancestor_p != ancestor_q:
        ancestor_p = ancestor_p.parent
        ancestor_q = ancestor_q.parent
    return ancestor_p


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def fst_common_anc(root: Node, node1: Node, node2: Node) -> Node:
    """return the first common ancestor of two nodes without using parent"""
    a, b, node = fst_anc_rec(root, node1, node2)
    return node


def fst_anc_rec(root: Node, node1: Node, node2: Node):

    left_found_n1, left_found_n2, left_anc = None, None, None
    right_found_n1, right_found_n2, right_anc = None, None, None
    if root.left:
        left_found_n1, left_found_n2, left_anc = fst_anc_rec(root.left, node1, node2)

    if root.right:
        right_found_n1, right_found_n2, right_anc = fst_anc_rec(
            root.right, node1, node2
        )

    if left_anc is not None:
        return left_found_n1, left_found_n2, left_anc
    if right_anc is not None:
        return right_found_n1, right_found_n2, right_anc

    found_n1 = left_found_n1 or right_found_n1
    found_n2 = left_found_n2 or right_found_n2

    ancestor = None
    if found_n1 and found_n2:
        ancestor = root

    found_n1 = found_n1 or root == node1
    found_n2 = found_n2 or root == node2

    return found_n1, found_n2, ancestor


t = BinaryTree()
n1 = t.insert(1, None)
n2 = t.insert(2, n1)
n3 = t.insert(3, n1)
n4 = t.insert(4, n2)
n5 = t.insert(5, n2)
n7 = t.insert(7, n3)
n8 = t.insert(8, n4)
n9 = Node(9)

test_cases = [
    (n3, n4, n1),
    (n3, n9, None),
]


def test_first_common_ancestor():
    for n_1, n_2, result in test_cases:
        assert result == first_common_ancestor(n_1, n_2)

    for n_1, n_2, result in test_cases:
        assert result == fst_common_anc(n1, n_1, n_2)


if __name__ == "__main__":
    test_first_common_ancestor()
