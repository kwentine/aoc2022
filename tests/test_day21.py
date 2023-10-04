from day21 import flatten, monkey_eval


def test_flatten():
    tree = {'root': 1}
    assert flatten(tree) == [1]
    tree = {'root': ('+', 'foo', 1),
            'foo': ('-', 3, 2)
            }
    assert flatten(tree) == ['+', '-', 3, 2, 1]
    tree = {
        'root': ('+', 'foo', 'humn'),
        'foo': ('-', 3, 'humn')
    }
    assert flatten(tree, 'humn') == ['+', '-', 3, 'humn', 'humn']


def test_monkey_eval():
    expr = [1]
    assert monkey_eval(expr) == 1
    expr = ['+', 1, 2]
    assert monkey_eval(expr) == 3
    expr = ['+', 1, '*', 'humn', 'humn']
    assert monkey_eval(expr, humn=2) == 5
