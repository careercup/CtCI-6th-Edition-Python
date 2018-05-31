"""
Exercise: 16.19 Pond sizes
Given a matrix representation of plot of land, find the sizes of all the ponds in the matrix.
0 indicates the water. Pond is the regionof water connected vertically, horizontally or diagonally.
"""


grid = [[0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]]


# helper function to compute a size of a pond recursively
def pond_region(grid, x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return 0

    if grid[x][y] != 0:
        return 0

    grid[x][y] = -1
    size = 1
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            if x != row or y != col:
                size += pond_region(grid, row, col)

    return size


# fuction to find all the pond sizes
def find_ponds(grid):
    result = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                result.append(pond_region(grid, i, j))

    return result


if __name__ == "__main__":
    pond_sizes = find_ponds(grid)
    print(', '.join(map(str, pond_sizes)))
