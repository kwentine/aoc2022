from functools import cache
from utils import read_input, ints
from tqdm import tqdm
from collections import defaultdict, deque

MINERALS = ORE, CLAY, OBS, GEO = range(4)
START_MINERALS = (0, 0, 0, 0)
START_ROBOTS = (1, 0, 0, 0)                                       
START_RESOURCES = tuple(zip(START_MINERALS, START_ROBOTS))
MAX_DEPTH = 24


def make_resources(minerals=START_MINERALS, robots=START_ROBOTS):
    return tuple(zip(minerals, robots))


def get_robots(resources):
    return tuple(j for (i, j) in resources)


def get_robot_count(kind, resources):
    return resources[kind][1]


def geodes(resources):
    return resources[GEO][0]


def harvest(resources):
    return tuple((i + j, j) for (i, j) in resources)


def build(resources, kind, recipe):
    return tuple((i - recipe[mineral], j + (kind == mineral)) for
            (mineral, (i, j)) in enumerate(resources))


def can_afford(resources, recipe):
    return all(i >= y for (i, _), y in zip(resources, recipe))


def may_accumulate(resources, blueprint):
    """Coudl it be useful to just accumulate resources?

    Yes, if it makes a robot recipe affordable in the future.
    """
    for recipe in blueprint:
        if can_afford(resources, recipe): continue
        robots = get_robots(resources)
        if all(r for (r, cost) in zip(robots, recipe) if cost):
            return True
    return False


def may_build(kind, resources, blueprint):
    """Should we try to build a particular robot ?

    Yes, if we don't already have enough robots to afford any
    recipe in one round for this particular mineral.
    """
    _, n_robots = resources[kind]
    return kind == GEO or any(recipe[kind] > n_robots for recipe in blueprint)


def parse(input_str: str):
    blueprints = []
    for line in input_str.strip().splitlines():
        _, *costs = ints(line)
        blueprints.append((
            (costs[0], 0, 0, 0),
            (costs[1], 0, 0, 0),
            (costs[2], costs[3], 0, 0),
            (costs[4], 0, costs[5], 0),
        ))
    return blueprints


def bfs(blueprint, start_state=START_RESOURCES, max_depth=MAX_DEPTH):
    todo = deque([(start_state, 0)])
    seen = {start_state}
    while todo:
        resources, t = todo.popleft()
        if t == max_depth:
            continue
        t += 1
        for s in neighbors(resources, blueprint):
            if s not in seen:
                seen.add(s)
                todo.append((s, t))
    return max(geodes(r) for r in seen)


def neighbors(resources, blueprint):
    h = harvest(resources)
    for (kind, recipe) in enumerate(blueprint):
        if can_afford(resources, recipe) and may_build(kind, resources, blueprint):
            yield build(h, kind, recipe)
    if may_accumulate(resources, blueprint):
        yield h


def part_one(data: list[tuple]) -> int:
    result = 0
    for i, blueprint in tqdm(list(enumerate(data, 1))):
        result += i * bfs(blueprint)
    return result


def part_two(data: list[tuple]) -> int:
    result = 1
    for blueprint in tqdm(data[:3]):
        result *= bfs(blueprint, max_depth=32)
    return result



if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_two(data))
