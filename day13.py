from utils import read_input
from functools import cmp_to_key
from itertools import chain

DAY = 13

def parse(input_str: str):
    return [[*map(eval, p.split())] for p in input_str.split("\n\n")]

def part_one(data: list) -> int:
    return sum(i * lt(l, r) for (i, (l, r)) in enumerate(data, 1))

def lt(l, r):
    todo = [(l, r)]
    while todo:
        l, r = todo.pop()
        if l == r:
            continue
        if isinstance(l, int) and isinstance(r, int):
            return l < r
        if isinstance(l, list) and isinstance(r, list):
            if not r:
                return False
            if not l:
                return True
            hl, *l = l
            hr, *r = r
            todo.extend([(l, r), (hl, hr)])
        else:
            l = l if isinstance(l, list) else [l]
            r = r if isinstance(r, list) else [r]
            todo.append((l, r))
    return 0


def part_two(data):
    dividers = [[[2]], [[6]]]
    packets = sorted(chain.from_iterable([dividers, *data]), key=cmp_to_key(cmp_lt))
    p = 1
    for (i, pack) in enumerate(packets, 1):
        if pack in dividers:
            p *= i
    return p

def cmp_lt(l, r):
    if l == r:
        return 0
    if lt(l, r):
        return -1
    return 1


def part_two_by_hand(data: str) -> int:
    dividers = [[[2]], [[6]]]
    packets = list(chain.from_iterable([dividers, *data]))
    packets = sort(packets, lt)
    p = 1
    for (i, x) in enumerate(packets, 1):
        if x in dividers:
            p *= i
    return p

def find_min(elts, lt):
    m = 0
    for (i, x) in enumerate(elts):
        if lt(x, elts[m]):
            m = i
    return m
        
def sort(elts, lt):
    sorted_elts = []
    while elts:
        i = find_min(elts, lt)
        sorted_elts.append(elts.pop(i))
    return sorted_elts


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
    print(part_two_by_hand(data))
