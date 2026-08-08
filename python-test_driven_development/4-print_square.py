#!/usr/bin/python3
"""Module that prints a square"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: length of the square's side.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
