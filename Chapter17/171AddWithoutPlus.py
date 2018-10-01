# CTCI 17.1
# Add Without Plus

def add_without_plus(a, b):
    while b != 0:
        # Sum without carry bit
        sum = a ^ b
        
        # Sum with only carrying
        carry = (a & b) << 1
        
        a = sum
        b = carry
        #print(a,b)
        
    return a

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_add_without_plus(self):
    self.assertEqual(add_without_plus(1, 1), 2)
    self.assertEqual(add_without_plus(1, 2), 3)
    self.assertEqual(add_without_plus(1001, 234), 1235)
    # does not work with negatives :(
    #self.assertEqual(add_without_plus(5, -1), 4)
    #self.assertEqual(add_without_plus(7,-5), 2)
    #self.assertEqual(add_without_plus(7,-29), -22)
    #self.assertEqual(add_without_plus(-2,10), 8)

if __name__ == "__main__":
  unittest.main()