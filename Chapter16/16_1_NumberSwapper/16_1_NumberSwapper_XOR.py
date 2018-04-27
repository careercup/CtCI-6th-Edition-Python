import unittest

def swap_numbers(a, b):
    a = a^b
    b = a^b # = (a^b)^b = a^(b^b) = a^0 = a
    a = a^b # = (a^b)^(a) = a^b^a = b^(a^a) = b^0 = b
    return a, b

class Test(unittest.TestCase):
    
    def test_small_big(self):
        pairs = [
            [1,2],
            [10,3],
            [4,4],
            [1,0],
            [7,-4],
            [-7,-4]
        ]
        for pair in pairs:
            a_original = pair[0]
            b_original = pair[1]
            a, b = swap_numbers(a_original, b_original)
            self.assertTrue(a == b_original)
            self.assertTrue(b == a_original)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
