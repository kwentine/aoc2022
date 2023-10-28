from utils import read_input, ints
from typing import Any
import re


def parse(input_str: str):
    chart, instructions = input_str.split("\n\n")
    grid = {}
    for x, line in enumerate(chart.splitlines(), 1):
        for y, c in enumerate(line.rstrip(), 1):
            if c == " ":
                continue
            grid[complex(x, y)] = c
    return grid, parse_moves(instructions)


def parse_moves(move_spec: str):
    return [m if m in "RL" else int(m) for m in re.findall(r"(R|L|\d+)", move_spec)]


def part_one(grid, moves) -> int:
    z = 1 + 51j
    v = 1j
    for mov in moves:
        if mov == "R":
            v *= -1j
        elif mov == "L":
            v *= 1j
        else:
            for _ in range(mov):
                nxt = z + v
                if nxt not in grid:
                    while nxt - v in grid:
                        nxt = nxt - v
                if grid[nxt] == ".":
                    z = nxt
                else:
                    break
    return 1000 * z.real + 4 * z.imag + [1j, 1, -1j, -1].index(v)


EDGE_SIZE = 50

# Oriented edges forming the contour of the flattened cube, defined by
# a starting point and a direction.
EDGES = [
    (1 + 51j, 1j),
    (1 + 101j, 1j),
    (1 + 150j, 1),
    (50 + 150j, -1j),
    (51 + 100j, 1),
    (101 + 100j, 1),
    (150 + 100j, -1j),
    (151 + 50j, 1),
    (200 + 50j, -1j),
    (200 + 1j, -1),
    (150 + 1j, -1),
    (101 + 1j, 1j),
    (100 + 51j, -1),
    (50 + 51j, -1),
]

# Correspondance between the contout edges. Example: headed out of
# edge 0 at distance t of its starting point, one reappears on edge 9
# at distance 50 - t of its starting point.
EDGE_PAIRS = ((0, 9), (1, 8), (2, 5), (3, 4), (6, 7), (10, 13), (11, 12))

EDGE_MAP = {**dict(EDGE_PAIRS), **dict((v, k) for (k, v) in EDGE_PAIRS)}


def on_edge(z, a, v):
    """Tests if Z is on the edge starting at A and oriented by V"""
    w = (z - a) * v.conjugate()
    return abs(z - a) <= EDGE_SIZE and w.real >= 0 and w.imag == 0


def wrap(z, v):
    """Return position and velocity after crossing an edge

    It is assumed that z is on an edge, and v is outbound.
    """
    idx, in_edge = next((i, e) for (i, e) in enumerate(EDGES) if on_edge(z, *e))
    out_edge = EDGES[EDGE_MAP[idx]]
    return _wrap(z, v, in_edge, out_edge)


def _wrap(z, vz, in_edge, out_edge):
    x, vx = in_edge
    y, vy = out_edge
    t = abs(z - x)
    return y + (EDGE_SIZE - 1 - t) * vy, vy * -1j


def part_two(grid, moves):
    z, v = 1 + 51j, 1j
    for m in moves:
        match m:
            case "R":
                v *= -1j
            case "L":
                v *= 1j
            case _:
                for _ in range(m):
                    nz, nv = z + v, v
                    if nz not in grid:
                        nz, nv = wrap(z, v)
                    if grid[nz] == ".":
                        z, v = nz, nv
                    else:
                        break
    return 1000 * z.real + 4 * z.imag + [1j, 1, -1j, -1].index(v)


if __name__ == "__main__":
    grid, moves = parse(read_input(ints(__file__)[-1]))
    print(part_one(grid, moves))
