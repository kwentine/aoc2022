from functools import cache
from utils import read_input, ints
from tqdm import tqdm
from collections import defaultdict, deque

MINERALS = ORE, CLAY, OBS, GEO = range(4)
START_MINERALS = (0, 0, 0, 0)
START_ROBOTS = (1, 0, 0, 0)                                       
START_RESOURCES = tuple(zip(START_MINERALS, START_ROBOTS))
MAX_DEPTH = 24

def max_robots(blueprint):
    return tuple(max(col) for col in zip(*blueprint))


def make_resources(minerals=START_MINERALS, robots=START_ROBOTS):
    return tuple(zip(minerals, robots))


def get_robots(resources):
    return tuple(j for (i, j) in resources)


def get_robot_count(kind, resources):
    return resources[kind][1]


def geodes(resources):
    return resources[GEO][0]


def harvest(resources, steps=1):
    return tuple((i + j * steps, j) for (i, j) in resources)


def build(resources, kind, recipe):
    return tuple((i - recipe[mineral], j + (kind == mineral)) for
            (mineral, (i, j)) in enumerate(resources))


def hoard_and_build(resources, kind, recipe, max_steps=MAX_DEPTH):
    steps = 0
    while not can_afford(resources, recipe):
        if steps == max_steps - 1:
            raise TimeoutError
        resources = harvest(resources)
        steps += 1
    return build(harvest(resources), kind, recipe), steps + 1


def can_afford(resources, recipe):
    return all(i >= y for (i, _), y in zip(resources, recipe))


def to_build(robots, blueprint):
    """Should we try to build a particular robot ?

    Yes, if we don't already have enough robots to afford any
    recipe in one round for this particular mineral.
    """
    geo = True
    obs = robots[OBS] < blueprint[GEO][OBS] and geo
    clay = robots[CLAY] < blueprint[OBS][CLAY] and obs
    ore = ((robots[ORE] < blueprint[CLAY][ORE] and clay)
           or (robots[ORE] < blueprint[OBS][ORE] and obs)
           or (robots[ORE] < blueprint[GEO][ORE] and geo))
    return (ore, clay, obs, geo)


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


def bfs(blueprint, start_resources=START_RESOURCES, max_depth=MAX_DEPTH):
    todo = deque([(start_resources, 0)])
    seen = {start_resources: 0}
    geo_max = 0
    geo_argmax = set()
    while todo:
        state = resources, t = todo.popleft()
        if t == max_depth:
            geo = resources[GEO][0]
            if geo == geo_max:
                geo_argmax.add(resources)
            elif geo > geo_max:
                geo_max = geo
                geo_argmax = {resources}
            continue
        for nr, nt in neighbors(state, blueprint, max_depth):
            if nr not in seen or seen[nr] > nt:
                seen[nr] = nt
                todo.append((nr, nt))
    return geo_max, geo_argmax


def neighbors(state, blueprint, max_depth):
    resources, t = state
    robots = get_robots(resources)
    max_steps = max_depth - t
    may_hoard = get_robot_count(GEO, resources)
    if can_afford(resources, blueprint[GEO]):
        n, dt = hoard_and_build(resources, GEO, blueprint[GEO], max_steps)
        yield n, t + dt
        return
    for (kind, build) in enumerate(to_build(robots, blueprint)):
        if not build and not kind == GEO: continue
        # Don't try to hoard if 
        if not all(robots[i] for (i, cost) in enumerate(blueprint[kind]) if cost): continue 
        try:
            n, dt = hoard_and_build(resources, kind, blueprint[kind], max_steps)
            yield n, t + dt
            may_hoard = False
        except TimeoutError:
            pass
    if may_hoard:
        yield harvest(resources, steps=max_steps), max_depth


def run(data, i, max_depth=MAX_DEPTH):
    blueprint = data[i]
    print(blueprint)
    g, winners = bfs(blueprint, max_depth=max_depth)
    print(list(winners)[:5])

        
def part_one(data: list[tuple]) -> int:
    result = 0
    for i, blueprint in tqdm(list(enumerate(data, 1))):
        g, _ = bfs(blueprint)
        result += i * g
    return result


def part_two(data: list[tuple]) -> int:
    result = 1
    for blueprint in tqdm(data[:3]):
        g, _ = bfs(blueprint, max_depth=32)
        result *= g
    return result


data = parse(read_input(ints(__file__)[-1]))

if __name__ == "__main__":
    run(data, 0, 32)
