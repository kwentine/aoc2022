from collections import defaultdict
from utils import read_input
from heapq import heappush, heappop
from math import inf

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
    distances = defaultdict(lambda: inf)
    visited = set()
    while todo:
        d, x = heappop(todo)
        if x == end:
            break
        for n in neighbors(*x):
            if grid[n] > grid[x] + 1 or (n in visited):
                continue
            if distances[n] > d + 1:
                distances[n] = d + 1
                heappush(todo, (d + 1, n))
        visited.add(x)
    return d
        

def part_two(data: str) -> int:
    start, end, grid = data
    todo = [(0, end)]
    distances = defaultdict(lambda: inf)
    visited = set()
    while todo:
        d, x = heappop(todo)
        if not grid[x]:
            break
        for n in neighbors(*x):
            if grid[n] < grid[x] - 1 or (n in visited):
                continue
            if distances[n] > d + 1:
                distances[n] = d + 1
                heappush(todo, (d + 1, n))
        visited.add(x)
    return d


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(data))
