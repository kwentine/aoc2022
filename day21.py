from utils import read_input, ints
from typing import Any
import operator as ops

ROOT = "root"
OPS = {
    '+': ops.add,
    '-': ops.sub,
    '*': ops.mul,
    '/': ops.floordiv
}

def parse(input_str: str):
    result = {}
    for line in input_str.splitlines():
        key, val = line.split(": ")
        try:
            val = int(val)
        except ValueError:
            l, op, r = val.split()
            val = op, l, r
        result[key] = val
    return result


def flatten(tree, variables=None, root=ROOT):
    variables = variables or []
    tree = {k: v for k, v in tree.items() if k not in variables}
    # ROOT could be a variable
    todo = [tree.get(ROOT, ROOT)]
    result = []
    while todo:
        node = todo.pop()
        if isinstance(node, int) or node in variables:
            result.append(node)
        else:
            op, l, r = node
            result.append(op)
            todo.append(tree.get(r, r))
            todo.append(tree.get(l, l))
    return result


def monkey_eval(expr, **variables):
    stack = []
    ptr = len(expr)
    while ptr:
        i = expr[ptr - 1]
        if i not in OPS:
            stack.append(variables.get(i, i))
        else:
            stack.append(OPS[i](stack.pop(), stack.pop()))
        ptr -= 1
    return stack.pop()


def part_one(data: Any) -> int:
    return monkey_eval(flatten(data))

def part_two(data):
    """Search for 'humn' by dichotomy

    The 'root' operation is transformed into a difference. We search
    for a value of 'humn' that makes it evaluate to 0.

    Observations show that v -> monkey_eval(expr, v) is positive and
    decreasing for small values of v.
    """
    _, l, r = data['root']
    data['root'] = ('-', l, r)
    expr = flatten(data, variables=['humn'])
    a, b = (0, 1)
    while v := monkey_eval(expr, humn=b) >= 0:
        a, b = b, 2 * b
    while 1:
        m = (a + b) // 2
        v = monkey_eval(expr, humn=m)
        if not v:
            return m
        if v > 0:
            a, b = m, b
        else:
            a, b = a, m

if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_two(data))
        
