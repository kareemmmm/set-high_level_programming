#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_all_same_values(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_two_elements(self):
        self.assertEqual(max_integer([7, 2]), 7)


if __name__ == '__main__':
    unittest.main()
