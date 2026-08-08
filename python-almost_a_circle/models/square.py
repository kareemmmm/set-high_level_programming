#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, updating both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the printable representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes of the Square using positional and keyword arguments."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
