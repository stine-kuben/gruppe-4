import pytest
from telling import er_like

@pytest.mark.parametrize("a,b,c,expected", [(1, 1, 1, True), (1, 1, 2, False), (1, 2, 1, False), (2, 1, 1, False), (1, 2, 3, False)])
def test_er_like(a, b, c, expected):
    assert er_like(a,b,c) == expected
