from random import random

class Node:
  def __init__(self, key):
    self.key = key
    self.parent = None
    self.left   = None
    self.l = 0
    self.right  = None
    self.r = 0

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.n = 0

  def insert(self, key):
    self.n += 1
    new = Node(key)
    if self.root is None:
      self.root = new
      return
    
    current = self.root
    while current:
      if current.key >= key:
        current.l += 1
        if current.left is None:
          current.left = new
          new.parent = current
          return
        else:
          current = current.left
      else:
        current.r += 1
        if current.right is None:
          current.right = new
          new.parent = current
          return
        else:
          current = current.right

  def getNode(self,key):
    current = self.root
    while current:
      if current.key == key:
        return current
      elif current.key > key:
        current = current.left
      else:
        current = current.right
    raise Exception("No such value in the tree")

  def randomNode(self):
    current = self.root
    # with probability 1/N = 1/(1+l+r) return node
    # with probability l/N go down left
    # with probability r/N go down right
    while current:
      N = current.r + current.l + 1.
      proba = random()
      if proba < 1/N:
        return current
      if proba < 1/N + current.l/N:
        current = current.left
      else:
        current = current.right

if __name__ == "__main__":
  bst  = BinarySearchTree()
  bst.insert(20)
  bst.insert(9);
  bst.insert(25);
  bst.insert(5);
  bst.insert(12);
  bst.insert(11);  
  bst.insert(14);    
  
  dict = {}
  for i in range(700000):
    node = bst.randomNode()
    if not node.key in dict.keys(): dict[node.key] = 0
    else: dict[node.key] += 1

  print(dict.values())
