import unittest
import math

class TreeNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.depth = None

class ListNode():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next

  def __str__(self):
    return str(self.data) + ',' + str(self.next)


def list_of_depths(tree):
    queue = []
    curr = tree
    result = []
    level = 0

    if curr:
        result.append([curr])
    else:
        return []

    while True:
        if not result[level]:
            break
        result.append([])
        for n in result[level]:
            if n.left:
                result[level+1].append(n.left)
            if n.right:
                result[level+1].append(n.right)
        level += 1
    return result


class Test(unittest.TestCase):
  def test_list_of_depths(self):
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = list_of_depths(node_a)
    self.assertEqual((lists[0]), [node_a])
    self.assertEqual((lists[1]), [node_b, node_c])
    self.assertEqual((lists[2]), [node_d, node_e, node_f])
    self.assertEqual((lists[3]), [node_h, node_g])

if __name__ == "__main__":
  unittest.main()
