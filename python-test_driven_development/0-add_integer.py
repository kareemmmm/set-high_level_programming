#!/usr/bin/python3
"""Module that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers or floats (each casted to an int).

    Args:
        a: first number (int or float).
        b: second number (int or float), default 98.

    Returns:
        int: the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")
    return a + b
