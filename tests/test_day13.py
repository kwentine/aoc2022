import pytest
from day13 import lt

@pytest.mark.parametrize("expected, l, r", [
    (1, [1,1,3,1,1],[1,1,5,1,1]),
    (1, [[1],[2,3,4]], [[1],4])
])
def test_lt(expected, l, r):
    assert lt(l, r) == expected 
