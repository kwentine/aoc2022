from day20 import *
import pytest


def values(head):
    return [i.value for i in head]


def to_string(head):
    return ", ".join(str(i) for i in head)


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
    head = make_list([1, 2, -3, 4, 0, 3, -2])
    assert head[0] is head
    zero = find(0, head)
    assert zero[1000].value == 4
    assert zero[2000].value == -3
    assert zero[3000].value == 2


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


@pytest.mark.parametrize(
    "n, before, after",
    [
        (1, [1, 2, -3, 3, -2, 0, 4], [2, 1, -3, 3, -2, 0, 4]),
        (2, [2, 1, -3, 3, -2, 0, 4], [1, -3, 2, 3, -2, 0, 4]),
        (-3, [1, -3, 2, 3, -2, 0, 4], [1, 2, 3, -2, -3, 0, 4]),
        (3, [1, 2, 3, -2, -3, 0, 4], [1, 2, -2, -3, 0, 3, 4]),
        (-2, [1, 2, -2, -3, 0, 3, 4], [1, 2, -3, 0, 3, 4, -2]),
        (0, [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 0, 3, 4, -2]),
        (4, [1, 2, -3, 0, 3, 4, -2], [1, 2, -3, 4, 0, 3, -2]),
        # Edge case
        (3, [3, 1, 2, 0], [3, 1, 2, 0]),
    ],
)
def test_move(n, before, after):
    head = make_list(before)
    item = find(n, head)
    move(item, item.value)
    head = find(after[0], head)
    assert values(head) == after


def test_mix():
    head = make_list([1, 2, -3, 3, -2, 0, 4])
    items = list(head)
    mix(items)
    assert values(head) == [1, 2, -3, 4, 0, 3, -2]
    assert values(find(0, head)) == [0, 3, -2, 1, 2, -3, 4]
    head = make_list([3, 1, 0])
    mix(list(head))
    assert values(head) == [3, 1, 0]


def test_part_one():
    assert part_one([1, 2, -3, 3, -2, 0, 4]) == 3
