from utils import read_input, ints


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
            next_attr = "nxt"
            incr = -1
        else:
            next_attr = "prev"
            incr = 1
        while n:
            res = getattr(res, next_attr)
            n += incr
        return res


def make_list(numbers):
    """Create a doubly linked list of integer items"""
    l = len(numbers)
    items = [Item(n) for n in numbers]
    for i, item in enumerate(items):
        item.nxt = items[(i + 1) % l]
        item.prev = items[i - 1]
    return items[0]


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


def wrap(value, length):
    if not length:
        return value
    value = value % length
    if value >= length // 2:
        value -= length
    return value


def move(head, steps):
    nxt = head.nxt
    remove(head)
    nxt = nxt[steps]
    insert_before(head, nxt)
    return head


def mix(items, times=1):
    length = len(items)
    for _ in range(times):
        for head in items:
            move(head, wrap(head.value, length - 1))


def part_one(data: list[int]) -> int:
    head = make_list(data)
    items = list(head)
    mix(items)
    zero = find(0, head)
    return sum(zero[i * 1000].value for i in (1, 2, 3))


def part_two(data: list[int]) -> int:
    head = make_list([i * 811589153 for i in data])
    items = list(head)
    mix(items, times=10)
    zero = find(0, head)
    return sum(zero[i * 1000].value for i in (1, 2, 3))


if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_two(data))
