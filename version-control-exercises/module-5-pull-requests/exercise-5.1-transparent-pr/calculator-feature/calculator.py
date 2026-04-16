"""Calculator module with basic arithmetic operations."""

import math
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a.

    Args:
        a: Number to subtract from.
        b: Number to subtract.

    Returns:
        The difference a - b.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.

    Args:
        a: First factor.
        b: Second factor.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b.

    Args:
        a: Dividend.
        b: Divisor (must not be zero).

    Returns:
        The quotient a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def percentage(value: Number, percent: Number) -> float:
    """Calculate a percentage of a value.

    Args:
        value: The base value.
        percent: The percentage to calculate.

    Returns:
        percent% of value.
    """
    return (value * percent) / 100


def square_root(a: Number) -> float:
    """Calculate the square root of a non-negative number.

    Args:
        a: A non-negative number.

    Returns:
        The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)
