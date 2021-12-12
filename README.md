# Pytest python

## Examples of using Pytest

We need to install `pytest` `pytest-xdist`:
```bash
pip install pytest
pip install pytest-xdist
```

### Commands in Terminal:
> running tests:
```bash
pytest -v
```

<br />

> running tests with @marks:
```bash
pytest -m xfail -v
```

<br />

> running tests, in the name of which you find *failure*:
```bash
pytest -k failure -v
```

<br />

> run the test and save the results to xml-file:
```bash
pytest test_multiply.py -v --junitxml=test-report.xml
```

<br />

> running 10 tests in parallel (`pytest-xdist`):
```bash
pytest -n10
```
