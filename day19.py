from functools import cache
from utils import read_input, ints
from tqdm import tqdm
from collections import defaultdict
from heapq import heappush, heappop

MINERALS = ORE, CLAY, OBS, GEO = range(4)


def harvest(state):
    minerals, robots = state
    return tuple(map(sum, zip(minerals, robots))), robots


def build(state, target, recipe):
    minerals, robots = state
    return (tuple(x - y for x, y in zip(minerals, recipe)),
            tuple(x + (y == target) for x, y in zip(robots, MINERALS)))


def should_harvest(state, blueprint):
    """Harvest if it makes a robot that is not already accessible accessible"""
    minerals, robots = state
    for (i, recipe) in enumerate(blueprint):
        if can_afford(state, recipe):
            continue
        if all(robots[j] for (j, cost) in enumerate(recipe) if cost):
            return True
    return False


def can_afford(state, recipe):
    minerals, _ = state
    return all(x >= y for x, y in zip(minerals, recipe))


def may_build_robot(m, state, blueprint):
    minerals, robots = state
    if m == ORE and robots[CLAY]:
        return False
    return True


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


def score(state, t):
    minerals, robots = state
    return t, -state[1][GEO]


def bfs_explorer(blueprint, tmax):

    def bfs(start_state):
        todo = [(score(start_state, 0), start_state, 0)]
        seen = {(start_state, 0)}
        geo_rbt = defaultdict(lambda: (0,))
        geo_max = set()
        while todo and len(geo_max) < 1:
            _, state, t = heappop(todo)
            minerals, robots = state
            if robots[-1:] < geo_rbt[t]:
                continue
            geo_rbt[t] = max(geo_rbt[t], robots[-1:])
            if t == tmax:
                geo_max.add(state[0][GEO])
            t += 1
            for s in neighbors(state, blueprint):
                if s not in seen:
                    seen.add(s)
                    heappush(todo, (score(s, t), s, t))
        return max(geo_max)

    return bfs


def neighbors(state, blueprint):
    h = harvest(state)
    for (i, recipe) in enumerate(blueprint):
        if can_afford(state, recipe):
            yield build(h, i, recipe)
    if should_harvest(state, blueprint):
        yield h


def extract(blueprint):

    @cache
    def explore(state, countdown):
        minerals, robots = state
        if not countdown:
            return minerals[GEO]
        countdown -= 1
        h = harvest(state)
        next_states = {h}
        for (i, recipe) in enumerate(blueprint):
            if can_afford(state, recipe) and may_build_robot(i, state, blueprint):
                ns = build(h, i, recipe)
                next_states.add(ns)
        return max(explore(s, countdown) for s in next_states)

    return explore


def part_one(data: list[tuple]) -> int:
    result = 0
    start = (0, 0, 0, 0), (1, 0, 0, 0)
    for i, blueprint in tqdm(list(enumerate(data, 1))):
        result += i * bfs_explorer(blueprint, 24)(start)
    return result


def part_two(data: list[tuple]) -> int:
    pass


if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_one(data))
