import re
from typing import Callable, Iterable
from utils import read_input
from collections import deque

DAY = 5

crate_line = re.compile(r"(   |\[.\]) ?" * 9)
move = re.compile(r"move (\d+) from ([1-9]) to ([1-9])\n")

CrateStacks = list[deque]
MoveInstructions = list[tuple[int, int, int]]

def parse(input_str: str) -> tuple[CrateStacks, MoveInstructions]:
    crates_str, moves_str = input_str.split("\n\n")
    return parse_crates(crates_str), parse_moves(moves_str)

def parse_crates(crates_str: str) -> CrateStacks:
    stacks = [deque() for _ in range(10)]
    for match in re.finditer(crate_line, crates_str):
        for (i, c) in enumerate(match.groups()):
            if c.strip():
                stacks[i].appendleft(c[1])
    return stacks

def parse_moves(moves_str: str) -> MoveInstructions:
    moves = []
    for match in re.finditer(move, moves_str):
        cnt, src, dest = map(int, match.groups())
        moves.append((cnt, src - 1, dest - 1))
    return moves

def part_one(data: tuple[CrateStacks, MoveInstructions]) -> str:
    crates, moves = data
    crates = simulate(crates, moves, lift_9000)
    return tops_of_the_stacks(crates)
        
def part_two(data: tuple[CrateStacks, MoveInstructions]) -> int:
    crates, moves = data
    crates = simulate(crates, moves, lift_9001)
    return tops_of_the_stacks(crates)

def lift_9000(stack: deque, n: int) -> Iterable[int]:
    return (stack.pop() for _ in range(n))

def lift_9001(stack: deque, n: int) -> list[int]:
    return reversed(list(lift_9000(stack, n)))

def simulate(crates: CrateStacks, moves: MoveInstructions, crane_lift: Callable) -> CrateStacks:
    for move in moves:
        cnt, src, dest = move
        crates[dest].extend(crane_lift(crates[src], cnt))
    return crates

def tops_of_the_stacks(crates: CrateStacks) -> str:
    return "".join(q[-1] for q in crates if q)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))

