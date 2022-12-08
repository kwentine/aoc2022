from utils import read_input
from collections import defaultdict, deque

DAY = 8

def parse(input_str: str):
    grid = {}
    for i, line in enumerate(input_str.splitlines()):
        for j, height in enumerate(line):
            grid[i, j] = int(height)
    return i, j, grid

def part_one(data: tuple[int, int, dict]) -> int:
    imax, jmax, grid = data
    return sum(visible(i, j, imax, jmax, grid) for (i, j) in grid)

def part_two(data: tuple[int, int, dict]) -> int:
    imax, jmax, grid = data
    return max(scenic_score(i, j, imax, jmax, grid) for (i, j) in grid)


def visible(i, j, imax, jmax, grid):
    height = grid[i, j]
    for line in directions (i, j, imax, jmax):
        for tree in line:
            if grid[tree] >= height:
                break
        else:
            return True
    return False

def scenic_score(i, j, imax, jmax, grid):
    height = grid[i, j]
    score = 1
    for line in directions(i, j, imax, jmax):
        distance = 0
        for tree in line:
            distance += 1
            if grid[tree] >= height:
                break
        score *= distance
    return score

def directions(i, j, imax, jmax):
    yield [(x, j) for x in range(i + 1, imax + 1)]
    yield [(x, j) for x in range(i - 1, -1, -1)]
    yield [(i, x) for x in range(j + 1, jmax + 1)]
    yield [(i, x) for x in range(j - 1, -1, -1)]


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
