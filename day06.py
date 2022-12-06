from utils import read_input
from io import IOBase, BytesIO
DAY = 6

def parse(input_str: str):
    return input_str.strip()

def scan_until_distinct(data: str, window: int) -> int:
    """Scan data until moving window consists of distinct characters"""
    i = 0
    while len(set(data[i:i+window])) != window:
        i += 1
    return i + window


def read_until_distinct(buff: IOBase, window: int) -> int:
    """Read input stream until moving window consists of distinct characters

    More in the spirit of the problem, this implementation reads bytes
    as they come and stores only the window of last seen elements, in
    a rotating buffer.
    """
    seen = bytearray(window)
    idx = 0
    while c := buff.read(1):
        seen[idx % window] = ord(c)
        idx += 1
        if len(set(x for x in seen if x)) == window:
            return idx

    raise ValuError(f"No distinct window of length {window}")


def part_one(data: str) -> int:
    return scan_until_distinct(data, 4)
    
def part_two(data: str) -> int:
    return scan_until_distinct(data, 14)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    print(part_two(data))
