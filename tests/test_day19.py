from day19 import (
    part_one, parse, wanted_robots,
    bfs, harvest, build, can_afford,
    make_resources, hoard_and_build
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

    
@pytest.mark.parametrize("kind, robots, blueprint, expected", ( 
    (0, (1, 0, 0, 0), B1, (1, 1, 1, 1)),
))
def test_to_build(kind, robots, blueprint, expected):
    assert wanted_robots(robots, blueprint) == expected

@pytest.mark.parametrize("minerals, robots, kind, recipe, exp_m, exp_r, exp_t", [
    ((0, 0, 0, 0), (1, 0, 0, 0), 0, (4, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), 5),
    ((0, 0, 0, 0), (1, 0, 0, 0), 0, (1, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), 2),
    ((4, 0, 0, 0), (1, 0, 0, 0), 0, (4, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), 1)
])
def test_hoard_and_build(minerals, robots, kind, recipe, exp_m, exp_r, exp_t):
    resources = make_resources(minerals, robots)
    r, dt = hoard_and_build(resources, kind, recipe)
    assert r == make_resources(exp_m, exp_r)
    assert dt == exp_t

def test_hoard_and_build_timeout():
    with pytest.raises(TimeoutError):
        resources = make_resources((0, 0, 0, 0), (1, 0, 0, 0))
        recipe = (1, 0, 0, 0)
        max_steps = 1
        hoard_and_build(resources, 0, recipe, 1)


@pytest.mark.parametrize("blueprint, expected", (
    (B1, 9),
    (B2, 12)
))
def test_bfs(blueprint, expected):
    g, winners = bfs(blueprint)
    assert g == expected


