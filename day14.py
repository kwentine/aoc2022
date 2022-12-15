import re
from collections import defaultdict
from typing import Iterable
from utils import read_input
from itertools import islice

DAY = 14

def ints(line: str) -> Iterable[int]:
    return map(int, re.findall(r"\d+", line))

def minmax(a, b):
    return min(a, b), max(a, b)

def parse(input_str: str):
    grid = defaultdict(int)
    bottom = 0
    for line in input_str.splitlines():
        it = ints(line)
        a, b = islice(it, 2)
        bottom = max(bottom, b)
        while p := list(islice(it, 2)):
            x, y = p
            bottom = max(bottom, y)
            x_min, x_max = minmax(x, a)
            y_min, y_max = minmax(y, b)
            for xx in range(x_min, x_max + 1):
                for yy in range(y_min, y_max + 1):
                    grid[xx, yy] = 1
            a, b = x, y
    return bottom, grid


def rest_point(grid, bottom):
    a, b = 500, 0
    while b < bottom + 1:
        for x, y in [(a, b + 1), (a - 1, b + 1), (a + 1, b + 1)]:
            if not grid[x, y]:
                a, b = x, y
                break
        else:
            return a, b
    return a, b

                    
def part_one(data: str) -> int:
    i = 0
    bottom, grid = data
    while 1:
        p = rest_point(grid, bottom)
        if p[1] == bottom + 1:
            return i
        grid[p] = 1
        i += 1
    return i

def part_two(data: str) -> int:
    i = 1
    bottom, grid = data
    while 1:
        p = rest_point(grid, bottom)
        if p == (500, 0):
            return i
        grid[p] = 1
        i += 1
    return i

if __name__ == "__main__":
    data = parse(read_input(DAY))
    print(part_one(data))
    data = parse(read_input(DAY))
    print(part_two(data))
