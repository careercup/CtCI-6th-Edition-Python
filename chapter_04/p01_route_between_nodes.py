import unittest
from collections import deque

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


def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False


def is_route_bfs(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == end:
                    return True
                else:
                    queue.append(adjacent)
        visited.add(node)
    return False


def is_route_bidirectional(graph, start, end):
    to_visit = deque()
    to_visit.append(start)
    to_visit.append(end)
    visited_start = set()
    visited_start.add(start)
    visited_end = set()
    visited_end.add(end)
    while to_visit:
        node = to_visit.popleft()

        if node in visited_start and node in visited_end:
            return True

        for y in graph[node]:
            if node in visited_start and y not in visited_start:
                visited_start.add(y)
                to_visit.append(y)
            if node in visited_end and y not in visited_end:
                visited_end.add(y)
                to_visit.append(y)
    return False


class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected

    def test_is_route_bidirectional(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bidirectional(self.graph, start, end)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
