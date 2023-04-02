import pytest
from day17 import rockfall_height, parse, draw

TEST_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

shifts = parse(TEST_INPUT)

@pytest.mark.parametrize("steps, height", [
    (1, 1),
    (2, 4),
    (3, 6),
])
def test_rockfall(steps, height):
    assert rockfall_height(shifts, steps)[1] == height


def test_draw():
    shifts = parse(TEST_INPUT)
    rubble, _ = rockfall_height(shifts, 10)
    expected = """\
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|"""
    assert draw(rubble) == expected
