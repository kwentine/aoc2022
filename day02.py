from utils import read_input

DAY = 2

A = ord("A")
X = ord("X")

def parse(input_str: str):
    rounds = []
    for elf, _, mine in input_str.splitlines():
        elf = ord(elf) - A
        mine = ord(mine) - X
        rounds.append((elf, mine))
    return rounds

def part_one(data: str) -> int:
    return sum(score(*match_round) for match_round in data)

def part_two(data: str) -> int:
    pass

def score(elf, mine):
    return (elf == (mine + 2) % 3) * 6 + (elf == mine) * 3 + mine + 1

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
