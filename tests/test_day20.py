from day20 import *
import pytest

def test_to_string():
    zero = Item(0)
    one = Item(1)
    zero.nxt = zero.prev = one
    one.nxt = one.prev = zero
    assert to_string(zero) == "0, 1"


def test_make_list():
    l = [1, 2, 3, 4]
    h = make_list(l)
    assert h.value == 1
    assert to_string(h) == "1, 2, 3, 4"


def test_gettitem():
    head = make_list(range(5))
    assert head[0] is head
    assert head[5] is head
    assert head[1].value == 1
    assert head[-2].value == 3


def test_remove():
    head = make_list(range(5))
    item = remove(head[2])
    assert item.value == 2
    assert to_string(head) == "0, 1, 3, 4"


def test_insert_before():
    head = make_list(range(5))
    item = Item("*")
    insert_before(item, head[3])
    assert to_string(head) == "0, 1, 2, *, 3, 4"

@pytest.mark.parametrize("n, before, after", [
    (1, [1, 2, -3, 3, -2, 0, 4], [2, 1, -3, 3, -2, 0, 4]),
    (2, [2, 1, -3, 3, -2, 0, 4], [1, -3, 2, 3, -2, 0, 4]),
    (-3, [1, -3, 2, 3, -2, 0, 4], [1, 2, 3, -2, -3, 0, 4]),
    (3, [1, 2, 3, -2, -3, 0, 4], [1, 2, -2, -3, 0, 3, 4]),
    (-2, [1, 2, -2, -3, 0, 3, 4], [1, 2, -3, 0, 3, 4, -2]),
    (0, [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 0, 3, 4, -2]),
    (4, [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 4, 0, 3, -2])
    
])
def test_mix(n, before, after):
    head = make_list(before)
    item = find(n, head)
    mix(item)
    head = find(after[0], head)
    assert values(head) == after


def test_mix_all():
    head = make_list([1, 2, -3, 3, -2, 0, 4])
    mix_all(list(head))
    assert values(head) == [1, 2, -3, 4, 0, 3, -2]


def test_part_one():
    assert part_one([1, 2, -3, 3, -2, 0, 4]) == 3
