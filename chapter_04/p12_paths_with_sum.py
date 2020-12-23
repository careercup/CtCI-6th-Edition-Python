from chapter_04.binary_tree import BinaryTree

# Brute Force O(NlogN)


def count_sum_paths(tree, target):
    if not isinstance(tree, BinaryTree):
        return None
    return _count_sum_paths(tree.root, target)


def _count_sum_paths(node, target_sum):
    if not node:
        return 0
    return (
        pathsfrom(node, target_sum)
        + _count_sum_paths(node.left, target_sum)
        + _count_sum_paths(node.right, target_sum)
    )


def pathsfrom(node, target_sum):
    if not node:
        return 0
    target_sum -= node.key
    counter = 0
    if target_sum == 0:
        counter += 1
    return (
        counter + pathsfrom(node.left, target_sum) + pathsfrom(node.right, target_sum)
    )


# Optimized O(N)


def count_sum_paths_optimized(tree, target_sum):
    if not isinstance(tree, BinaryTree):
        return None
    return _count_sum_paths_optimizied(tree.root, target_sum)


def _count_sum_paths_optimizied(node, target_sum, running=0, hashtable=None):
    if hashtable is None:
        hashtable = {}
    if not node:
        return 0
    running += node.key
    total = hashtable.get(running - target_sum, 0)
    if running == target_sum:
        total += 1
    increment(hashtable, running, 1)
    left_count = _count_sum_paths_optimizied(node.left, target_sum, running, hashtable)
    right_count = _count_sum_paths_optimizied(
        node.right, target_sum, running, hashtable
    )
    total += left_count + right_count
    increment(hashtable, running, -1)
    return total


def increment(hashmap, key, delta):
    hashmap.setdefault(key, 0)
    hashmap[key] += delta
    if hashmap[key] == 0:
        hashmap.pop(key)


if __name__ == "__main__":
    t1 = BinaryTree()
    n1 = t1.insert(10, None)
    n2 = t1.insert(5, n1)
    n3 = t1.insert(-3, n1)
    n4 = t1.insert(3, n2)
    n5 = t1.insert(2, n2)
    n6 = t1.insert(3, n4)
    n7 = t1.insert(-2, n4)
    n8 = t1.insert(1, n5)
    n9 = t1.insert(11, n3)
    n10 = t1.insert(8, n9)
    n11 = t1.insert(-8, n10)

    print(count_sum_paths(t1, 8))
    print(count_sum_paths(t1, 6))
    print(count_sum_paths_optimized(t1, 8))
    print(count_sum_paths_optimized(t1, 6))
