#!/usr/bin/python3
"""Defines a MagicClass matching the provided bytecode."""

import math


class MagicClass:
    """Represents a circle with radius logic derived from bytecode."""

    def __init__(self, radius=0):
        """Initialize MagicClass with validation."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate and return the circumference."""
        return 2 * math.pi * self.__radius
