import unittest

def generate_valid_pairs_of_parentheses(n):
    def helper(open_parentheses_remaining,
               closed_parentheses_remaining,
               current_string):
        if len(current_string) == n*2:
            result.append(current_string)
        if open_parentheses_remaining > 0:
            helper(open_parentheses_remaining-1,
                   closed_parentheses_remaining,
                   current_string+'(')
        if closed_parentheses_remaining > open_parentheses_remaining:
            helper(open_parentheses_remaining,
                   closed_parentheses_remaining-1,
                   current_string+')')
    result = []
    helper(n, n, '')
    return result

class TestSuite(unittest.TestCase):
    def test_null(self):
        self.assertEqual(generate_valid_pairs_of_parentheses(0),
                         [''])

    def test_single_pair(self):
        self.assertEqual(generate_valid_pairs_of_parentheses(1),
                         ['()'])

    def test_two_pairs(self):
        self.assertEqual(sorted(generate_valid_pairs_of_parentheses(2)),
                         sorted(['()()', '(())']))

    def test_three_pairs(self):
        self.assertEqual(sorted(generate_valid_pairs_of_parentheses(3)),
                         sorted(["((()))","(()())","(())()","()(())","()()()"]))

    def test_four_pairs(self):
        self.assertEqual(sorted(generate_valid_pairs_of_parentheses(4)),
                         sorted(["(((())))","((()()))","((())())","((()))()",
                                 "(()(()))","(()()())","(()())()","(())(())",
                                 "(())()()","()((()))","()(()())","()(())()",
                                 "()()(())","()()()()"]))

    def test_five_pairs(self):
        self.assertEqual(sorted(generate_valid_pairs_of_parentheses(5)),
                         sorted(["((((()))))","(((()())))","(((())()))",
                                 "(((()))())","(((())))()","((()(())))",
                                 "((()()()))","((()())())","((()()))()",
                                 "((())(()))","((())()())","((())())()",
                                 "((()))(())","((()))()()","(()((())))",
                                 "(()(()()))","(()(())())","(()(()))()",
                                 "(()()(()))","(()()()())","(()()())()",
                                 "(()())(())","(()())()()","(())((()))",
                                 "(())(()())","(())(())()","(())()(())",
                                 "(())()()()","()(((())))","()((()()))",
                                 "()((())())","()((()))()","()(()(()))",
                                 "()(()()())","()(()())()","()(())(())",
                                 "()(())()()","()()((()))","()()(()())",
                                 "()()(())()","()()()(())","()()()()()"]))

if __name__ == '__main__':
    unittest.main()
