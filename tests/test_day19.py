from day19 import part_one, parse, extract, may_build_robot, bfs_explorer
import pytest

INPUT = """\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian.
"""

START_SATE = (0, 0, 0, 0), (1, 0, 0, 0)

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

@pytest.mark.parametrize("blueprint, expected", (
    (B1, 9),
    (B2, 12)
))
def test_bfs_eplorer(blueprint, expected):
    assert bfs_explorer(blueprint, 24)(START_SATE) == expected


@pytest.mark.skip
@pytest.mark.parametrize("blueprint, expected", (
    (B1, 9),
    (B2, 12)
))
def test_extract(blueprint, expected):
    assert extract(blueprint)(START_SATE, 24) == expected

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


