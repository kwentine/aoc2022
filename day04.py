import re
from utils import read_input

DAY = 4

pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)\n")

RangePair = tuple[int, int, int, int]

def parse(input_str: str) -> list[RangePair]:
    return [tuple(int(n) for n in match.groups())
            for match in re.finditer(pattern, input_str)]

def part_one(data: list[RangePair]) -> int:
    # Inclusion occurs if the bounds for the group is one on the range pairs
    return sum((min(bounds), max(bounds)) in (bounds[:2], bounds[2:])
               for bounds in data)
        
def part_two(data: list[RangePair]) -> int:
    # The tow possible disjoint configurations are:
    #     a1----b1            |            a1---b1
    #               a2----b2  |   a2---b2
    # So we are looking for cases where !(b1 < a2 || a1 > b2),
    # condition that is expanded below using De Morgan's law
    return sum((b1 >= a2) and (a1 <= b2)
               for (a1, b1, a2, b2) in data)

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))

