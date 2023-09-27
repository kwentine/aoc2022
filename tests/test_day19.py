from day19 import (
    part_one, parse, may_build,
    bfs, harvest, build, can_afford,
    make_resources, may_accumulate
)
                   
import pytest

INPUT = """\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian.
"""

B1 = (
    (4, 0, 0, 0),
    (2, 0, 0, 0),
    (3, 14, 0, 0),
    (2, 0, 7, 0),
)

B2 = (
    (2, 0, 0, 0),
    (3, 0, 0, 0),
    (3, 8, 0, 0),
    (3, 0, 12, 0),
)

@pytest.mark.parametrize("resources, expected", [
    [(), ()],
    [((0, 1), (1, 2)), ((1, 1), (3, 2))],
])
def test_harvest(resources, expected):
    assert harvest(resources) == expected


@pytest.mark.parametrize("minerals, kind, recipe, leftovers, robots", [
    [(3, 14, 0, 0), 2, (3, 14, 0, 0), (0, 0, 0, 0), (1, 0, 1, 0)],
    [(5, 6, 15, 0), 3, (3, 0, 12, 0), (2, 6, 3, 0), (1, 0, 0, 1)],
])
def test_build(minerals, kind, recipe, leftovers, robots):
    actual = build(make_resources(minerals), kind, recipe)
    expected = make_resources(leftovers, robots)
    assert actual == expected

    
@pytest.mark.parametrize("minerals, recipe, expected", [
    [(1, 5, 6, 7), (4, 0, 0, 0), False],
    [(10, 2, 7, 1), (2, 0, 7, 0), True]
])
def test_can_afford(minerals, recipe, expected):
    assert can_afford(make_resources(minerals), recipe) == expected

@pytest.mark.parametrize("minerals, robots, blueprint, expected", [
    [(0, 0, 0, 0), (1, 0, 0, 0), B1, True],
    [(2, 0, 0, 0), (1, 0, 0, 0), B1, True],
    [(5, 0, 0, 0), (1, 0, 0, 0), B1, False],
])
def test_may_accumulate(minerals, robots, blueprint, expected):
    resources = make_resources(minerals, robots)
    assert may_accumulate(resources, blueprint) == expected
    
    
@pytest.mark.parametrize("blueprint, expected", (
    (B1, 9),
    (B2, 12)
))
def test_bfs(blueprint, expected):
    assert bfs(blueprint) == expected

@pytest.mark.skip    
@pytest.mark.parametrize("m, state, blueprint, expected", ( 
    (0, ((1, 0, 0, 0), (1, 0, 0, 0)), B1, True),
))
def test_may_build_robot(m, state, blueprint, expected):
    assert may_build_robot(m, state, blueprint) == expected

@pytest.mark.skip
def test_part_one():
    blueprints = parse(INPUT)
    assert part_one(blueprints) == 33


