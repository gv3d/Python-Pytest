# тести для функції division в utils.py
from utils import division
import pytest

@pytest.mark.parametrize("a, b, result", [(10, 5, 2),  # - параметризація для тесту test_division
                                     (20, 2, 10),
                                     (10, -2, -5),
                                     (5, 2, 2.5)])

def test_division(a, b, result):
    assert division(a, b) == result


def test_zero_division():  #  - тест ділення на нуль
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


def test_type_error():  #  - тест ділення на некоректний тип даних
    with pytest.raises(TypeError):
        division(10, '5')


@pytest.mark.parametrize('expected_error, divider', [(ZeroDivisionError, 0),  #  - параметризація тестів для підняття помилки
                                                     (TypeError, '5')])

def test_zero_division(expected_error, divider):
    with pytest.raises(expected_error):
        division(10, divider)