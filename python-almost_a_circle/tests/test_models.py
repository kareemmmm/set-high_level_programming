#!/usr/bin/python3
"""Unit tests skeleton for base, rectangle, and square modules."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""
    def test_id_generation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_explicit_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""
    def test_rectangle_creation(self):
        r = Rectangle(10, 2, 1, 1, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 5)

    def test_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""
    def test_square_creation(self):
        s = Square(5, 2, 3, 9)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 9)


if __name__ == "__main__":
    unittest.main()
