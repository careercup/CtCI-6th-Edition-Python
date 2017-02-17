"""Robot in a grid.
Design a path for a robot through (r rows, c columns) where there are obstacles.
Robot can only move right and down.
Return path.

Input = dense r x c matrix of obstacles: [rows... [columns...] ]
Output = List of steps: ["R", "D", "R"...]

Options:
Think about a binary tree: R or D at each node.  Depth-first search.
Stop when we get to the end of the grid: we only need one solution.
When we get to the end of the grid, return path.
"""


class Robot(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.path = []

    def is_path(self, r=0, c=0):
        self.path.append((r, c))

        # Terminate: end
        if r == len(self.matrix) - \
                1 and c == len(self.matrix[r]) - 1 and (self.matrix[r][c] != "X"):
            return True

        # Terminate: going off grid
        if r == len(self.matrix) or c == len(self.matrix[r]):
            self.path.pop()
            return False

        # Terminate: obstacle
        if self.matrix[r][c]:
            self.path.pop()
            return False

        # Recurse
        if (self.is_path(r + 1, c)) or (self.is_path(r, c + 1)):
            return True
        else:
            self.path.pop()
            return False

matrix = [[None, "X", None, None],
          [None, "X", None, "X"],
          [None, None, None, None],
          ["X", None, "X", None]]

robot = Robot(matrix)
if robot.is_path():
    print("There is a path:", robot.path)
else:
    print("There is no path")
