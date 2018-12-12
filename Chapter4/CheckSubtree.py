class Node:
  def __init__(self, key):
    self.key = key
    self.parent = None
    self.left   = None
    self.right  = None

  def __eq__(self,other):
    if not isinstance(other,Node): return False
    return self.key == other.key and self.left == other.left and self.right == other.right 


class BinaryTree:
  def __init__(self):
    self.root = None

  def __eq__(self,other):
    if not isinstance(other,BinaryTree): return False
    return self.root == other.root

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

def checksubtree(t1,t2):
  if not t1 or not t2: return False
  return check(t1.root,t2.root)

def check(n1,n2):
  if n1 == n2: return True
  if n1 == None or n2 == None: return False
  return check(n1.left,n2) or check(n1.right,n2)


if __name__ == "__main__":
  t1 = BinaryTree()
  n1 = t1.insert(1,None)
  n2 = t1.insert(2,n1)
  n3 = t1.insert(3,n1)
  n4 = t1.insert(4,n2)
  n5 = t1.insert(5,n2)
  n7 = t1.insert(7,n3)
  n8 = t1.insert(8,n4) 

  t2 = BinaryTree()
  n40 = t2.insert(4,None)
  n80 = t2.insert(8,n40) 
  #n90 = t2.insert(9,n40) 

  print(checksubtree(t1,t2))
