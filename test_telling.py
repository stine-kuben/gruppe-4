import pytest
from telling import doblet

@pytest.mark.parametrize("liste,expected", [([1, 2, 3], [2, 4, 6]), ([-1, 2, 0], [-2, 4, 0])])
def test_dobling(liste, expected):
    assert doblet(liste) == expected
