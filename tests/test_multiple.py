import pytest

@pytest.mark.parametrize('x, y, z', [(1, 2, 3),
                                     (2, 2, 4),
                                     (5, 4, 10),
                                     (10, -10, 0),])
def test_some(x, y, z):
    assert x + y == z