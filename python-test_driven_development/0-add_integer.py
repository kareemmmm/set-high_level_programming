#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The sum as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
