# tests/test_core.py
import pytest

from fibonacci_tdd_kata.core import fibonacci_opti


@pytest.mark.parametrize(("n", "expected"), [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_first_cases(n: int, expected):
    assert fibonacci_opti(n) == expected


def test_bigger_value():
    assert fibonacci_opti(10) == 55
    assert fibonacci_opti(50) == 12586269025
    assert fibonacci_opti(100) == 354224848179261915075


def test_fibo_rejects_invalid_input() -> None:
    with pytest.raises(ValueError):
        fibonacci_opti(-1)
