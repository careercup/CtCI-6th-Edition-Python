# Solution with recursion O(2^r+c)
def get_path(maze):
    if not maze:
        return None
    path = []
    if is_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return None


def is_path(maze, row, col, path):
    # if out of bounds or not available, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # if there's a path from the start to here, add my location
    if (
        is_at_origin
        or is_path(maze, row, col - 1, path)
        or is_path(maze, row - 1, col, path)
    ):
        point = (row, col)
        path.append(point)
        return True

    return False


# Solution with memoization
def get_path_memoized(maze):
    if not maze:
        return None
    path = []
    failed_points = set()
    if is_path_memoized(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


def is_path_memoized(maze, row, col, path, failed_points):
    # If out of bounds or not availabe, return
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    point = (row, col)

    # if we've already visisted this cell, return
    if point in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location
    if (
        is_at_origin
        or is_path_memoized(maze, row, col - 1, path, failed_points)
        or is_path_memoized(maze, row - 1, col, path, failed_points)
    ):
        path.append(point)
        return True

    failed_points.add(point)
    return False


def find_path(grid: list) -> list:
    path = []
    visited = {}
    return _find_path(grid, 0, 0, path, visited)[0]


def _find_path(grid: list, r: int, c: int, path: list, visited: list) -> tuple:
    path.append((r, c))
    visited[r, c] = 1
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return path, True
    for dr, dc in ((1, 0), (0, 1)):
        if (
            r + dr < len(grid)
            and c + dc < len(grid[0])
            and not (r + dr, c + dc) in visited
            and grid[r + dr][c + dc]
        ):
            path, found_path = _find_path(grid, r + dr, c + dc, path, visited)
            if found_path:
                return path, True
    path.pop()
    return path, False


def test_path():
    testable_functions = [get_path, get_path_memoized, find_path]
    grid = [
        [True, True, True, False, True],
        [False, True, False, True, True],
        [True, True, True, True, True],
    ]
    path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4)]
    for f in testable_functions:
        assert f(grid) == path


if __name__ == "__main__":
    test_path()
