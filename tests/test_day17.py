import pytest
from day17 import rockfall, parse, draw

TEST_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

shifts = parse(TEST_INPUT)

@pytest.mark.parametrize("steps, height", [
    (1, 1),
    (2, 4),
    (3, 6),
    (2022, 3068)
])
def test_rockfall(steps, height):
    assert rockfall(shifts, steps)[1] == height


def test_draw():
    shifts = parse(TEST_INPUT)
    rubble, _ = rockfall(shifts, 10)
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
