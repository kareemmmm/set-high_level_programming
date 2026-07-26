#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """MyInt class inheriting from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
