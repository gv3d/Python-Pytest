import pytest
import math

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def test_square(funk):
    num = 7
    assert funk * 7 == 42

@pytest.mark.others
def test_quality():
    assert 10 == 11
