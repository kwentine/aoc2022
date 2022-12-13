from collections import defaultdict
from utils import read_input
from collections import deque

DAY = 12

a = ord("a")

def parse(input_str: str):
    grid = defaultdict(lambda: 27)
    for i, line in enumerate(input_str.splitlines()):
        for j, c in enumerate(line):
            if c == "S":
                start = i, j
                c = "a"
            elif c == "E":
                end = i, j
                c = "z"
            grid[i, j] = ord(c) - a
    return start, end, grid
            
def neighbors(i, j):
    return [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1)
    ]

def part_one(data: str) -> int:
    start, end, grid = data
    todo = [(0, start)]
    seen = {start}
    while todo:
        dist, x = todo.pop(0)
        if x == end:
            return dist
        for n in neighbors(*x):
            if grid[n] > grid[x] + 1 or (n in seen):
                continue
            todo.append((dist + 1, n))
            seen.add(n)
        

def part_two(data: str) -> int:
    start, end, grid = data
    todo = deque([(0, end)])
    seen = {end}
    while todo:
        d, x = todo.popleft()
        if not grid[x]:
            return d
        for n in neighbors(*x):
            if grid[n] < grid[x] - 1 or (n in seen):
                continue
            seen.add(n)
            todo.append((d + 1, n))


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
