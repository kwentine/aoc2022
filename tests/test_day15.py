import pytest
import pytest
import day15 as d


def test_example():
    input_str = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    data = d.parse(input_str)
    assert d.part_one(data, level=10) == 26 
    assert d.part_two(data, bound=20) == 56000011
@pytest.mark.parametrize("x, level, expected", [
    ((0, 0, 1, 0), 0, {0, 1, -1}),
    ((8, 7, 2, 10), -2, {8}),
    ((8, 7, 2, 10), -10, set()),
    ((8, 7, 2, 10), -1, {7, 8, 9}),
    
])
def test_trace(x, level, expected):
    assert d.trace(*x, level=level) == expected
