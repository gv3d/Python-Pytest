import pytest
import math

# pytest test_failure.py

def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 6

def test_square_failure():
    num = 7
    assert num ** 2 == 40

def test_equality_failure():
    assert 10 == 11