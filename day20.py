from utils import read_input, ints
from typing import Any

def parse(input_str: str):
    return ints(input_str)

class Item:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.nxt = nxt
        self.prev = prev
        
    def __str__(self):
        return str(self.value)
    
    def __iter__(self):
        yield self
        current = self.nxt
        while current is not self:
            yield current
            current = current.nxt

    def __getitem__(self, n):
        if not n:
            return self
        res = self
        if n > 0:
            next_attr = 'nxt'
            incr = -1
        else:
            next_attr = 'prev'
            incr = 1
        while n:
            res = getattr(res, next_attr)
            n += incr
        return res


def find(value, head):
    for item in head:
        if item.value == value:
            return item

def remove(item):
    item.prev.nxt = item.nxt
    item.nxt.prev = item.prev
    item.nxt = item.prev = None
    return item


def insert_before(item, other):
    other.prev.nxt = item
    item.prev = other.prev
    item.nxt = other
    other.prev = item
    return item


def make_list(numbers):
    """Create a doubly linked list"""
    l = len(numbers)
    items = [Item(n) for n in numbers]
    for (i, item) in enumerate(items):
        item.nxt = items[(i + 1) % l]
        item.prev = items[i - 1]
    return items[0]


def mix(item):
    other = item[item.value]
    if item.value > 0:
        after, before = other, other.nxt
    else:
        after, before = other.prev, other
    if item not in (after, before):
        remove(item)
        insert_before(item, before)
    return item


def mix_all(items):
    for item in items:
        mix(item)
    
def to_string(head):
    return ", ".join(str(i) for i in head)

def values(head):
    return [i.value for i in head]

def part_one(data: Any) -> int:
    head = make_list(data)
    print(data[-10:])
    mix_all(list(head))
    zero = find(0, head)
    x = zero[1000]
    y = x[1000]
    z = y[1000]
    return x.value + y.value + z.value

def part_two(data: Any) -> int:
    pass

if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_one(data))
    
    
