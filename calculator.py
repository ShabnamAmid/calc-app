"""Basic calculator operations."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def percent(number):
    """Convert a percentage value to its decimal representation."""
    return number / 100


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def sqrt(number):
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return math.sqrt(number)


square_root = sqrt
