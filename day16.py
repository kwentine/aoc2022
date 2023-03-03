from utils import read_input, ints
from collections import namedtuple
from heapq import heappop, heappush
import re

DAY = 16

State = namedtuple("State", "released, valve, opened, elapsed")

def valves(line: str):
    return re.findall("[A-Z][A-Z]", line)

def parse(input_str: str):
    tunnels = {}
    rates = {}
    for line in input_str.splitlines():
        valve, *neighbors = valves(line)
        flow, = ints(line)
        tunnels[valve] = neighbors
        rates[valve] = flow
    return tunnels, rates


def neighbors(state, rates, tunnels):
    # We stay, and open a new valve
    released, elapsed, valve, opened = state
    if opened: 
        released -= sum(rates[v] for v in opened.split(':'))
    elapsed += 1
    if valve not in opened and rates[valve]:
        opened = opened + (':' if opened else "") + valve
        yield (released, elapsed, valve, opened)
    for end_of_tunnel in tunnels[valve]:
        yield (released, elapsed, end_of_tunnel, opened)

def part_one(data: str) -> int:
    tunnels, rates = data
    start = (0, 0, "AA", "")
    todo = [start]
    seen = set()
    while 1:
        state = heappop(todo)
        print(state)
        if state[1] == 30:
            return state[0]
        for ns in neighbors(state, rates, tunnels):
            heappush(todo, ns)


def part_two(data: str) -> int:
    pass

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
