from utils import read_input

DAY = 9

STEPS = {
    "D": (0, -1),
    "U": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}
DIAGONALS = (
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)       
)

Step = tuple[int, int]
Point = tuple[int, int]

def parse(input_str: str) -> list[int, int]:
    moves = []
    for line in input_str.splitlines():
        step, count = line.split()
        step = STEPS[step]
        count = int(count)
        moves.extend(step for _ in range(count))
    return moves

def neighborhood(p: Point, diagonals=True):
    steps = [(0, 0), *STEPS.values()]
    if diagonals:
        steps.extend(DIAGONALS)
    return {(p[0] + dx, p[1] + dy) for (dx, dy) in steps}

    
def follow(head: Point, tail: Point) -> Point:
    if tail not in neighborhood(head, diagonals=True):
        try:
            tail, = neighborhood(head, diagonals=False) & neighborhood(tail)
        except ValueError:
            tail, = neighborhood(head) & neighborhood(tail)
    return tail

def simulate_rope(size):
    seen = {(0, 0)}
    rope = [(0, 0) for _ in range(size)]
    for dx, dy in data:
        rope[0] = rope[0][0] + dx, rope[0][1] + dy
        for i in range(1, size):
            rope[i] = follow(rope[i - 1], rope[i])
        seen.add(rope[size - 1])
    return len(seen)

    
def part_one(data: str) -> int:
    return simulate_rope(size=2)

def part_two(data: str) -> int:
    return simulate_rope(size=10)

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
