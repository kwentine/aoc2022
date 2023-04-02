from utils import read_input
from itertools import cycle

def parse(input_str: str):
    return [int(c == ">") or -1 for c in input_str.strip()]

SHAPES = (
    (0, 1, 2, 3),
    (1j, 1, 1 + 1j, 1 + 2j, 2 + 1j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 1j, 2j, 3j),
    (0, 1, 1j, 1 + 1j)
)

def rockfall_height(jets: list[int], n: int):
    """Return height of the rubble after n rocks have fallen"""
    max_height = 0
    fallen = 0
    jet_cycle_length = len(jets)
    jets = enumerate(cycle(jets))
    rocks = cycle(SHAPES)
    rubble = set(range(8))
    while fallen < n:
        start_offset = 3 + (max_height + 4) * 1j
        rock = next(rocks)
        rock = {c + start_offset for c in rock}
        while 1:
            j, dx = next(jets)
            shifted_rock = {c + dx for c in rock}
            if all(0 < c.real < 8 for c in shifted_rock) and not (shifted_rock & rubble):
                rock = shifted_rock
            fallen_rock = {c - 1j for c in rock}
            if fallen_rock & rubble:
                rubble |= rock
                max_height = max(max_height, int(max(c.imag for c in rock)))
                fallen += 1
                # Expermientally found that after one cycle of jets
                # has been completed, the heigh increases by 2613
                # every 1715 rocks. Hence the shortcut.
                if (n - fallen) % 1715 == 0 and j > jet_cycle_length:
                    return rubble, max_height + (n - fallen) // 1715 * 2613
                break
            rock = fallen_rock
    return rubble, max_height
            

def draw(rubble, truncate=0):
    max_height = int(max(r.imag for r in rubble))
    grid = [list("|.......|") for _ in range(max_height)]
    for c in rubble:
        x, y = int(c.real), int(c.imag)
        if y:
            grid[y - 1][x] = "#"
    return "\n".join("".join(row) for row in reversed(grid))


def part_one(data: str) -> int:
    rubble, max_height = rockfall_height(data, 2022)
    return max_height


def part_two(data: str) -> int:
    rubble, max_height = rockfall_height(data, 1000000000000)
    return max_height


if __name__ == "__main__":
    DAY = int(__file__[-5:-3])
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
