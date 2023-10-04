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


def flatten(tree, *variables, root=ROOT):
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
    while expr:
        i = expr.pop()
        if i not in OPS:
            stack.append(variables.get(i, i))
        else:
            stack.append(OPS[i](stack.pop(), stack.pop()))
    return stack.pop()


def humn_influence(data):
    # root: bjgs + tjtt
    data['humn'] = 'humn'
    data['root'] = ('-', 'bjgs', 'tjtt')
    expr = flatten(data, variables=('humn',))
    for humn in range(10):
        res = monkey_eval(expr[:], humn=humn)
        print(f"{humn=} {res=}")
    data['root'] = ('+', 'bjgs', 'tjtt')
    expr = flatten(data, variables=('humn',))
    assert monkey_eval(expr[:], humn=105) == 145167969204648
        

def part_one(data: Any) -> int:
    return monkey_eval(flatten(data))


def part_two(data: Any) -> int:
    pass


if __name__ == "__main__":
    data = parse(read_input(ints(__file__)[-1]))
    print(part_one(data))
        
