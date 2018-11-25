from BinarySearchTree import BinarySearchTree
from BinaryTree import BinaryTree

def validateBST(bst):
  if bst.root == None:
    return True
  return check(bst.root, None, None)

def check(node, min, max):
  if not node:
    return True
  else: print(min, node.key, max)
  if (min and node.key < min) or (max and node.key >= max):
    return False
  return check(node.left, min, node.key) and check(node.right, node.key, max)



if __name__ == "__main__":
  bst  = BinarySearchTree()
  bst.insert(20)
  bst.insert(9);
  bst.insert(25);
  bst.insert(5);
  bst.insert(12);
  bst.insert(11);  
  bst.insert(14);    

  t = BinaryTree()
  n1 = t.insert(5,None)
  n2 = t.insert(4,n1)
  n3 = t.insert(6,n1)
  n4 = t.insert(3,n2)
  n5 = t.insert(6,n2)
  n7 = t.insert(5,n3)
  n8 = t.insert(2,n4) 
  
  false = validateBST(t)
  true  = validateBST(bst)
