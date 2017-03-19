""" Cracking the coding interview 6th Edition.
Finding all the permutations of a string with unique charactrers. """

def permutation_without_dups(prefix, inp):
  #Recursion - base condition.
  if not inp:
    print ''.join(prefix)
  for i in xrange(0, len(inp)):
     permutation_without_dups(prefix + list(inp[i]), list(inp[0:i]) + list(inp[i + 1:len(inp)]))


#Driver program to test permutations
if __name__ == "__main__":
        permutation_without_dups([], list("abc"))
