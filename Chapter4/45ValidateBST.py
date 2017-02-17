class CheckBST(object):
    """Check if a binary tree is a BST.
    BST property: every node on the left < every node on the right.

            4                           4
        2       6	= True;         2       6	= False
       1 3     5 7                3 1     7 5
    """

    def __init__(self, edges):
        self.edges = edges

    def check_children(self, node):
        """Check BST property using a DFS."""
        children = self.edges[node]
        property = True
        if not children:
            return property
        left = children[0]
        right = children[1]
        if left:
            property &= left < node
            property &= self.check_children(left)
        if right:
            property &= node < right
            property &= self.check_children(right)
        return property

if __name__ == "__main__":
    cb = CheckBST([None, None, [1, 3], None, [2, 6], None, [5, 7], None])
    print(cb.check_children(4))
    cb = CheckBST([None, None, [3, 1], None, [2, 6], None, [7, 5], None])
    print(cb.check_children(4))
