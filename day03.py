import string
from utils import read_input

DAY = 3

score_table = "🎄" + string.ascii_lowercase + string.ascii_uppercase

def parse(input_str: str):
    return input_str.splitlines()

def part_one(data: list[str]) -> int:
    total = 0
    for rucksack in data:
        l = len(rucksack)
        misplaced, = set(rucksack[:l // 2]) & set(rucksack[l // 2:])
        total += score_table.index(misplaced)
    return total

def part_two(data: str) -> int:
    total = 0
    while data:
        a, b, c = (set(data.pop()) for _ in range(3))
        badge, = a & b & c
        total += score_table.index(badge)
    return total

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
