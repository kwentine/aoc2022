import pytest
from day22 import parse, on_edge

TEST_DATA = """\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def test_parse():
    grid, mov = parse(TEST_DATA)
    assert 1j + 1 not in grid
    assert 9j + 1 in grid
    assert 4j + 5 in grid and grid[4j + 5] == "#"
    assert mov == [10, "R", 5, "L", 5, "R", 10, "L", 4, "R", 5, "L", 5]

def test_on_edge():
    assert on_edge(51j, 51j, 1j)
