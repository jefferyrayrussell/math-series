import pytest


@pytest.mark.parametrize('n, result', [(-1, False), (3, 2), (4, 3), (5, 5)])
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', [(-1, False), (3, 4), (4, 7), (5, 11)])
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', [(3, 2), (4, 3), (5, 5)])
def test_sum_series(n, result):
    from series import sum_series
    assert sum_series(n) == result

@pytest.mark.parametrize('n, a, b, result', [(3, 2, 1, 4), (4, 2, 1, 7), (5, 2, 1, 11)])
def test_sum_series_lucas(n, a, b, result):
    from series import sum_series
    assert sum_series(n, a, b) == result

