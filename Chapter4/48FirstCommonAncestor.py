from BinaryTree import BinaryTree

def firstcommonancestor(bt,p,q):
  if not p or not q:
    return
  depth_p = bt.get_depth(p)
  depth_q = bt.get_depth(q)
  delta = abs(depth_p-depth_q)
  if depth_p < depth_q:
    for i in range(delta):
      q = q.parent
  elif depth_q < depth_p:
    for i in range(delta):
      p = p.parent
  ancestorp = p
  ancestorq = q
  while ancestorp != ancestorq:
    ancestorp = ancestorp.parent
    ancestorq = ancestorq.parent
  return ancestorp
    
if __name__ == "__main__":
  t = BinaryTree()
  n1 = t.insert(1,None)
  n2 = t.insert(2,n1)
  n3 = t.insert(3,n1)
  n4 = t.insert(4,n2)
  n5 = t.insert(5,n2)
  n7 = t.insert(7,n3)
  n8 = t.insert(8,n4) 

  ancestor = firstcommonancestor(t,n3,n4)
  print(ancestor.key)

# method in class BinaryTree:
#  def get_depth(self,node):
#    current = node.parent
#    depth = 0
#    while current:
#      current = current.parent
#      depth += 1
#    return depth
