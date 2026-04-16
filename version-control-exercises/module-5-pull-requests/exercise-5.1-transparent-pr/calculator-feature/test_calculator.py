"""Tests for the calculator module."""

from calculator import add, subtract, multiply, divide, percentage, square_root
import pytest


def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert abs(add(0.1, 0.2) - 0.3) < 1e-9


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 3) == pytest.approx(2.333, rel=1e-2)
    assert divide(-6, 3) == -2.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_percentage():
    assert percentage(200, 10) == 20.0
    assert percentage(50, 50) == 25.0
    assert percentage(100, 100) == 100.0


def test_square_root():
    assert square_root(9) == 3.0
    assert square_root(0) == 0.0
    assert square_root(2) == pytest.approx(1.414, rel=1e-2)


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-1)
