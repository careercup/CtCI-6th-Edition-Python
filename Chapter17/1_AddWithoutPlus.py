import unittest

def add(addend_a, addend_b):
    if addend_b == 0:
        return addend_a

    sum = addend_a ^ addend_b
    carry = (addend_a & addend_b) << 1

    return add(sum, carry)

class Test(unittest.TestCase):
    def test_add_without_plus(self):
        self.assertEqual(add(1, 3), 4)
        self.assertEqual(add(123456789, 123456789), 123456789 * 2) 

if __name__ == "__main__":
    unittest.main()

