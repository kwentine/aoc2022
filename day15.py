from utils import read_input, ints

DAY = 15
Y = 2_000_000

def l1(x, y, a, b):
    return abs(x - a) + abs(y - b)

def parse(input_str: str):
    return [*map(ints, input_str.splitlines())]

def trace(x, y, a, b, level=Y):
    radius = l1(x, y, a, b)
    proj = l1(x, y, x, level)
    freedom = radius - proj
    return set(range(x - freedom, x + freedom + 1))

def trace_bounds(x, y, a, b, level=Y):
    radius = l1(x, y, a, b)
    proj = l1(x, y, x, level)
    freedom = radius - proj
    xmin = x - freedom
    xmax = x + freedom
    if b == level:
        xmin += (a == xmin)
        xmax -= (a == xmax)
    return (xmin, xmax) if xmin <= xmax else tuple()

def union(intervals, a , b):
    disjoint = []
    overlap = [(a, b)]
    for x, y in intervals:
        if y < a or b < x:
            disjoint.append((x, y))
        else:
            overlap.append((x, y))
    xmin = min(a for a, _ in overlap)
    xmax = max(b for _, b in overlap)
    disjoint.append((xmin, xmax))
    return [*sorted(disjoint)]

def length(a, b):
    return b - a + 1
    

def part_one(data, level=Y):
    intervals = []
    for x in data:
        bounds = trace_bounds(*x, level=level)
        if bounds:
            intervals = union(intervals, *bounds)
    return sum(length(*i) for i in intervals)
        

def part_two(data: str, bound=4_000_000) -> int:
    beacons = {(a, b) for (_, _, a, b) in data}
    for level in range(bound + 1):
        intervals = []
        for x in data:
            bounds = trace_bounds(*x, level=level)
            if bounds:
                intervals = union(intervals, *bounds)
        if intervals != union(intervals, 0, bound):
            print(level, " searching ...")
            candidates = set(range(bound + 1)) - {a for (a, b) in beacons if b == level} 
            for (a, b) in intervals:
                candidates -= set(range(a, b+1))
            if candidates:
                x, = candidates
                return x * 4_000_000 + level
        
if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one_bis(data))
    print(part_two(data))
