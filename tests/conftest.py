# conftest.py - містить фікстури для наших тестів
import pytest

@pytest.fixture
def input_2():
    input = 39
    return input

@pytest.fixture
def funk():
    n = 6
    return n
