from utils import read_input

DAY = 11


MONKEYS = [
    {
        "items": [77, 69, 76, 77, 50, 58],
        "operation": lambda old: old * 11,
        "test": (5, 1, 5),
    },
    {
        "items": [75, 70, 82, 83, 96, 64, 62],
        "operation": lambda old: old + 8,
        "test": (17, 5, 6),
    },
    {
        "items": [53],
        "operation": lambda old: old * 3,
        "test": (2, 0, 7)
    },
    {
        "items": [85, 64, 93, 64, 99],
        "operation": lambda old: old + 4,
        "test": (7, 7, 2)
    },

    {
        "items": [61, 92, 71],
        "operation": lambda old: old * old,
        "test": (3, 2, 3),
    },
    {
        "items": [79, 73, 50, 90],
        "operation": lambda old: old + 2,
        "test": (11, 4, 6),
    },

    {
        "items": [50, 89],
        "operation": lambda old: old + 3,
        "test": (13, 4, 3),
    },
    {
        "items": [83, 56, 64, 58, 93, 91, 56, 65],
        "operation": lambda old: old + 5,
        "test": (19, 1, 0)
    }
]

MOD = 5 * 17 * 2 * 7 * 3 * 11 * 13 * 19

def parse(input_str: str):
    monkey_list = []
    for spec in input_str.split("\n\n"):
        monkey_list.append(parse_monkey(spec))

def part_one() -> int:
    business = [0] * 8
    for rnd in range(20):
        print(f"Round {rnd}")
        for i, monkey in enumerate(MONKEYS):
            print(f"  Monkey {i}")
            business[i] += inspect(monkey)
    business.sort()
    return business[-1] * business[-2]

def part_two() -> int:
    business = [0] * 8
    for rnd in range(10_000):
        for i, monkey in enumerate(MONKEYS):
            business[i] += inspect_mod(monkey)
    business.sort()
    return business[-1] * business[-2]


def inspect(monkey) -> int:
    inspected = len(monkey["items"])
    new = [item // 3 for item in map(monkey["operation"], monkey["items"])]
    div, true_dest, false_dest = monkey["test"]
    for item in new:
        dest = true_dest if not (item % div) else false_dest
        MONKEYS[dest]["items"].append(item)
    monkey["items"] = []
    return inspected

def inspect_mod(monkey) -> int:
    inspected = len(monkey["items"])
    new = [item % MOD for item in map(monkey["operation"], monkey["items"])]
    div, true_dest, false_dest = monkey["test"]
    for item in new:
        dest = true_dest if not (item % div) else false_dest
        MONKEYS[dest]["items"].append(item)
    monkey["items"] = []
    return inspected



if __name__ == "__main__":
    print(part_two())
