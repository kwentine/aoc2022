from functools import cache
from utils import read_input, ints
from tqdm import tqdm

MINERALS = ORE, CLAY, OBS, GEO = range(4)

def harvest(state):
    minerals, robots = state
    return tuple(map(sum, zip(minerals, robots))), robots

def build(state, target, recipe):
    minerals, robots = state
    return (tuple(x - y for x, y in zip(minerals, recipe)),
            tuple(x + (y == target) for x, y in zip(robots, MINERALS)))

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
        _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = ints(line)
        blueprints.append((
            # TODO: The second tuple is redundant, use the index
            (ore_ore, 0, 0, 0),
            (clay_ore, 0, 0, 0),
            (obs_ore, obs_clay, 0, 0),
            (geo_ore, 0, geo_obs, 0),
        ))
    return blueprints


def score(robots):
    return tuple(-i for i in reversed(robots))


from collections import deque, defaultdict
from heapq import heappush, heappop
def bfs_explorer(blueprint, tmax):

    def bfs(start_state):
        todo = [(score(start_state[1]), start_state, 0)]
        seen = {(start_state, 0)}
        best_so_far = defaultdict(int)
        geo_max = 0
        while todo:
            _, state, t = heappop(todo)
            minerals, robots = state
            if t == tmax:
                geo_max = max(geo_max, state[0][GEO])
                continue
            if robots[GEO] < best_so_far[t]:
                continue
            t += 1
            for s in neighbors(state, blueprint):
                minerals, robots = s
                if robots[GEO] < best_so_far[t]:
                    continue
                best_so_far[t] = max(best_so_far[t], robots[GEO])
                if (s, t) not in seen:
                    seen.add((s, t))
                    heappush(todo, (score(robots), s, t))
        return geo_max

    return bfs


def neighbors(state, blueprint):
    h = harvest(state)
    for (i, recipe) in enumerate(blueprint):
        if can_afford(state, recipe):
            yield build(h, i, recipe)
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
