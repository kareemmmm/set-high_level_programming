#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation."""

    def __init__(self, size):
        """Initializes size as a private positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
