from utils import read_input, ints, l1
from itertools import combinations
from collections import deque


def parse(input_str: str):
    i = iter(ints(input_str))
    return set(zip(i, i, i))


def neighbors(p):
    x, y, z = p
    return (
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    )


def part_one(data: list) -> int:
    faces = len(data) * 6
    for c1, c2 in combinations(data, 2):
        if l1(c1, c2) == 1:
            faces -= 2
    return faces


import itertools


def part_two(data: set) -> int:
    free = {(0, 0, 0)}
    trapped = set()
    faces = part_one(data)
    # Find all trapped air cubes
    for p in itertools.product(range(20), range(20), range(20)):
        if p in data:
            continue
        bfs(p, free, trapped, data)
    # Remove faces touching trapped air cubes
    for p in data:
        for q in trapped:
            if l1(p, q) == 1:
                faces -= 1
    return faces


def bfs(start, free, trapped, rock):
    if start in (free | trapped):
        return
    todo = deque([start])
    seen = {start}
    while todo:
        p = todo.popleft()
        for n in neighbors(p):
            if n in rock:
                continue
            if n in free:
                free |= seen | set(todo)
                return
            if n not in seen:
                seen.add(n)
                todo.append(n)
    trapped |= seen


if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_two(data))
