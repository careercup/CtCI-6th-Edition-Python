class Node:
  def __init__(self, key):
    self.key = key
    self.parent = None
    self.left   = None
    self.right  = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, key, parent):
    new = Node(key)
    if parent == None:
      if self.root is None:
        self.root = new
        return new
      raise Exception("a root already exists")
    else: 
      if not parent.left: 
        parent.left = new
        new.parent = parent
      elif not parent.right:
        parent.right = new
        new.parent = parent
      else:
        raise Exception("a node cannot have more than two children")            
    return new

# Brute Force O(NlogN)

def countpath(t,target):
  if not isinstance(t,BinaryTree): return
  return count(t.root,target)

def count(node,target):
  if not node: return 0
  return pathsfrom(node,target) + count(node.left,target) + count(node.right,target)

def pathsfrom(node,target):
  if not node: return 0
  target -= node.key
  counter = 0
  if target == 0: counter+=1
  return counter + pathsfrom(node.left,target) + pathsfrom(node.right,target)   

# Optimized O(N)

def opticountpath(t,target):
  if not isinstance(t,BinaryTree): return
  return count(t.root,target)

def opticount(node,target,running=0,hashtable={}):
  if not node: return 0
  running += node.key
  total = hashtable.get(running-target,0)
  if running == target:
    total += 1
  increment(hashmap,running,1)
  leftcount  = opticount(node.left ,target,running,hashtable)
  rightcount = opticount(node.right,target,running,hashtable)
  total += leftcount + rightcount
  increment(hashmap,running,-1)
  return total


def increment(hashmap,key,delta):
  hashmap.setdefault(key, 0) 
  hashmap[key] += delta
  if hashmap[key] == 0: hashmap.pop(key)

if __name__ == "__main__":
  t1 = BinaryTree()
  n1 = t1.insert(10,None)
  n2 = t1.insert(5,n1)
  n3 = t1.insert(-3,n1)
  n4 = t1.insert(3,n2)
  n5 = t1.insert(2,n2)
  n6 = t1.insert(3,n4)
  n7 = t1.insert(-2,n4)
  n8 = t1.insert(1,n5)
  n9 = t1.insert(11,n3)
  n10 = t1.insert(8,n9)
  n11 = t1.insert(-8,n10)

#  counter = countpath(t1,8)

  counter = opticountpath(t1,6)
  print(counter)
