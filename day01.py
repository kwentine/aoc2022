from utils import read_input

DAY = 1

def parse(input_str: str) -> list[list[int]]:
    result = []
    for elf in input_str.split("\n\n"):
        calories = [int(l) for l in elf.splitlines()]
        result.append(calories)
    return result

def part_one(data: str) -> int:
    return max(sum(elf) for elf in data)

def part_two(data: str) -> int:
    pass

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
