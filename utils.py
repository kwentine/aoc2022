import re

def read_input(day: int) -> str:
    with open(f"data/day{day:02d}.txt") as f:
        return f.read()

def ints(line: str) -> list[int]:
    return [int(i) for i in re.findall(r"\d+", line)]
    
    
