'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''
import unittest

# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R


def is_route(graph, start, end, visited=[]):
    for node in graph[start]:
        if node not in visited:
            visited = visited + [node]
            if node == end or is_route(graph, node, end, visited):
                return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    graph = {'A':['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D':['B', 'C'],
    'E': ['C', 'F'],
    'F': ['E', 'O', 'I', 'G'],
    'G': ['F', 'H'],
    'H': ['G'],
    'I': ['F', 'J'],
    'O': ['F'],
    'J': ['K', 'L', 'I'],
    'K': ['J'],
    'L': ['J'],
    'P': ['Q', 'R'],
    'Q': ['P', 'R'],
    'R': ['P', 'Q'],
    }

    tests = [
        ('A', 'L', True),
        ('A', 'B', True),
        ('H', 'K', True),
        ('L', 'D', True),
        ('Q', 'G', False),
        ('R', 'A', False),
        ('P', 'B', False)
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
