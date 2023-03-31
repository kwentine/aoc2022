import pytest
from day16 import *

TEST_INPUT = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


def test_parse():
    input_str = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA"""
    expected = ({"AA": ["DD", "II", "BB"], "BB": ["CC", "AA"]}, {"BB": 13})
    assert parse(input_str) == expected


tunnels, rates = parse(TEST_INPUT)


@pytest.mark.parametrize("start, end , d", [("AA", "JJ", 2), ("AA", "EE", 2)])
def test_distance(start, end, d):
    dist = bfs_dist(tunnels)
    assert dist("AA", "JJ") == 2


def test_part_one():
    data = parse(TEST_INPUT)
    expected = 1651
    actual = part_one(data)
    assert actual == expected


def test_part_two():
    data = parse(TEST_INPUT)
    expected = 1707
    actual = part_two(data)
    assert actual == expected
