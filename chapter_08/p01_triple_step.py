import unittest

def solution(n): # Time: O(n) | Space: O(1)
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    a = solution(0)
    b = solution(1)
    c = solution(2)
    result = 0
    for _ in range(3, n+1):
        result = c + b + a
        a = b
        b = c
        c = result
    
    return result

class Test(unittest.TestCase):
    tribonacci_numbers = [
        1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 
        10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 
        2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 
        181997601, 334745777, 615693474, 1132436852
    ]

    def test(self):
        for n in range(len(self.tribonacci_numbers)):
            self.assertEqual(self.tribonacci_numbers[n], solution(n))

if __name__ == "__main__":
    unittest.main()