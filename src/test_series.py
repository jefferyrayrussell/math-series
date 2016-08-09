import pytest


@pytest.mark.parametrize('n, result', [(-1, False), (3, 2), (4, 3), (5, 5)])
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', [(-1, False), (3, 4), (4, 7), (5, 11)])
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result
