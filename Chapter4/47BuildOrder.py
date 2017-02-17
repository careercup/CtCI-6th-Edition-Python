"""Given a list of project dependencies, determine the build order for a project.
If no build order is possible, return an error.

Model as tree, where dependencies are leaves.
Sparse, so store in adjacency list.
Detect cycle by doing Depth-First Search from root & adding visited nodes to list.
If cyclical dependencies, throw error.
"""


class DependencyTree:

    def __init__(self, tree):
        self.tree = tree  # {"a":["b","c","d"]}
        self.root = "a"
        self.visited = []

    def built_ok(self, node=None):
        if node is None:
            node = self.root
        if node in self.visited:  # cycle
            return False
        self.visited.append(node)
        if node not in self.tree or self.tree[node] == []:
            # no dependencies
            return True
        is_ok = True
        for child in self.tree[node]:
            # dependencies
            is_ok &= self.built_ok(child)
        return is_ok

    def build_order(self):
        return_value = self.visited.copy()
        return_value.reverse()
        return return_value


if __name__ == "__main__":
    should_pass = DependencyTree({"a": ["b", "c"], "b": ["d", "e"], "c": ["f"]})
    print("Pass:", should_pass.built_ok())
    print("Build order:", should_pass.build_order())
    should_fail = DependencyTree({"a": ["b", "c"], "b": ["d", "e", "a"], "c": ["f"]})
    print("Fail:", should_fail.built_ok())
