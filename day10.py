from utils import read_input

def parse(input_str: str):
    return input_str.splitlines()

def simulate(inupt_str):
    clock = 0
    value = 1
    for inst in data:
        # We enter the first cycle
        clock += 1
        yield clock, value
        if inst == "noop":
            continue
        # We enter the second cycle
        clock += 1
        yield clock, value
        value += int(inst.split()[1])
    yield clock + 1, value

def part_one(data: list[str]) -> int:
    score = 0
    for i, value in simulate(data):
        if ((i % 40) == 20) and i < 221:
            score += i * value
    return score

def part_two(data: str) -> int:
    screen = [["."] * 40 for _ in range(6)]
    for (cycle, value) in simulate(data):
        col = (cycle - 1) % 40
        row = (cycle - 1) // 40
        if col in (value - 1, value, value + 1):
            screen[row][col] = "#"
    return "\n".join("".join(row) for row in screen)
              
              

if __name__ == "__main__":
    day = int(__file__.split(".")[0][-2:])
    data = parse(read_input(day))
    print(part_two(data))
