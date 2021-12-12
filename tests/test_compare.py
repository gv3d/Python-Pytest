import pytest

@pytest.mark.xfail  # — декоратор-маркер, не включає результат виконання тесту в загальний звіт
@pytest.mark.great  # — декоратор-маркер, команда "pytest -m great -v" запускає всі тести з цім маркером 'great'
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.skip  # — декоратор-маркер, пропускає цей тест
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
