from utils import read_input
from pathlib import Path

from collections import defaultdict

DAY = 7

TOTAL_DISK_SPACE = 70000000
MIN_FREE_SPACE = 30000000

ROOT = Path("/")

def parse(input_str: str):
    file_sizes = defaultdict(dict)
    path = ROOT
    for line in input_str.splitlines():
        cmd = line.split()
        if cmd[0] == "$":
            if cmd[1] == "ls": continue
            # Changing current directory
            path = (path / Path(cmd[2])).resolve()
        # Process `ls` output
        else:
            kind, name = cmd
            if kind != "dir":
                file_sizes[path / name] = int(kind)
    return du(file_sizes)

def du(file_sizes: dict[Path, int]) -> dict[Path, int]:
    """Compute disk usage by directory"""
    directory_sizes = defaultdict(int)
    for path, size in file_sizes.items():
        for parent in path.parents:
            directory_sizes[parent] += size
    return directory_sizes

def part_one(directory_sizes: dict[Path, int]) -> int:
    return sum(size for size in directory_sizes.values() if size <= 100000)

def part_two(directory_sizes: dict[Path, int]) -> int:
    free_space = TOTAL_DISK_SPACE - directory_sizes[ROOT]
    missing_space = MIN_FREE_SPACE - free_space
    return min(size for size in directory_sizes.values() if size >= missing_space)
    

if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
