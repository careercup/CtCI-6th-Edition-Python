from BinarySearchTree import BinarySearchTree

def BSTsequences(bst):
  if not bst.root:
    return []
  return helper(bst.root)

def helper(node):
  if not node:
    return [[]]
  else:
    right_sequences = helper(node.right)
    left_sequences  = helper(node.left)
    sequences = []
    for right in right_sequences:
      for left in left_sequences:
        sequences = weave(left,right, [node.key], sequences)
    return sequences


def weave(first, second, prefix, results):
  if len(first) == 0 or len(second) == 0:
    result = prefix.copy()
    result.extend(first)
    result.extend(second)
    results.append(result)
    return results
  else:
    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results



first = []
second = []
prefix = [0]
results = []
counter = 0
results = weave(first, second, prefix, results)
#for result in results:
#  print(result)

if __name__ == "__main__":
  bst  = BinarySearchTree()
  bst.insert(20)
  bst.insert(9);
  bst.insert(25);
  bst.insert(5);
  bst.insert(12);
  #bst.insert(11);  
  #bst.insert(14);    


  sequences = BSTsequences(bst)
  print(sequences)
