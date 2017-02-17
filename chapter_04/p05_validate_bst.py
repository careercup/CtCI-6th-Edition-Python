def is_binary_search_tree(node, edges):
    children = edges[node]
    property = True
    if not children:
        return property
    left = children[0]
    right = children[1]
    if left:
        property &= left < node
        property &= is_binary_search_tree(left, edges)
    if right:
        property &= node < right
        property &= is_binary_search_tree(right, edges)
    return property


if __name__ == "__main__":
    """
         4                          4
     2       6    = True;       2       6    = False
    1 3     5 7                3 1     7 5
    """
    print(
        is_binary_search_tree(4, [None, None, [1, 3], None, [2, 6], None, [5, 7], None])
    )
    print(
        is_binary_search_tree(4, [None, None, [3, 1], None, [2, 6], None, [7, 5], None])
    )
