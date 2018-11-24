from BinaryTree import BinaryTree

def listdepth(t):
  if t.root == None:
    return
  ll = []
  prev = [t.root]
  while len(prev) > 0:
    ll.append(prev)
    current = []
    for node in prev:
      if node.left : current.append(node.left)
      if node.right: current.append(node.right)
    prev = current
  return ll

t  = BinaryTree()
n1 = t.insert(1,None)
n2 = t.insert(2,n1)
n3 = t.insert(3,n1)
n4 = t.insert(4,n2)
n5 = t.insert(5,n2)
n7 = t.insert(7,n3)
n8 = t.insert(8,n4)

ll = listdepth(t)
print([[node.key for node in l] for l in ll])
