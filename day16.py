from functools import cache
from itertools import permutations
from collections import deque
from utils import read_input, ints
from functools import cache
from collections import namedtuple
from heapq import heappop, heappush

import itertools
import re

DAY = 16


def parse(input_str: str) -> tuple[dict, dict]:
    tunnels = {}
    rates = {}
    for line in input_str.splitlines():
        valve, *neighbors = re.findall("[A-Z][A-Z]", line)
        (flow,) = ints(line)
        tunnels[valve] = neighbors
        if flow:
            rates[valve] = flow
    return tunnels, rates


def bfs_dist(graph: dict[str, list[str]], directed=False):
    @cache
    def distance(start: str, end: str):
        if not directed and start > end:
            return distance(end, start)

        todo = deque([(start, 0)])
        seen = set(start)
        while todo:
            node, d = todo.popleft()
            for neighbor in graph[node]:
                if neighbor == end:
                    return d + 1
                if neighbor not in seen:
                    seen.add(neighbor)
                    todo.append((neighbor, d + 1))
        raise ValueError(f"No path found from {start} to {end}")

    return distance


def key(valves):
    return " ".join(sorted(valves))


def generate_paths_with_release(start, rates, dist, countdown):
    best_subset_releases = {}

    todo = [([start], countdown, 0)]
    done = []
    while todo:
        path, t, released = todo.pop()
        k = key(path[1:])
        best_subset_releases[k] = max(best_subset_releases.get(k, 0), released)
        extensions = []
        for v in rates:
            if v in path:
                continue
            d = dist(path[-1], v)
            if d < t:
                time_left = t - d - 1
                extensions.append(
                    ([*path, v], time_left, released + time_left * rates[v])
                )
        if extensions:
            todo.extend(extensions)
    return best_subset_releases


def part_one(data: str) -> int:
    tunnels, rates = data
    dist = bfs_dist(tunnels)
    best_releases = generate_paths_with_release("AA", rates, dist, 30)
    return max(best_releases.values())


def part_two(data: str) -> int:
    tunnels, rates = data
    dist = bfs_dist(tunnels)
    best_releases = generate_paths_with_release("AA", rates, dist, 26)
    return max(
        best_releases[player_valves] + best_releases[elephant_valves]
        for player_valves, elephant_valves in itertools.combinations(best_releases, 2)
        if not set(player_valves.split()) & set(elephant_valves.split())
    )


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(data))
