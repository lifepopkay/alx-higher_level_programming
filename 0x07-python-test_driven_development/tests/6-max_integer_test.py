#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestInteger(unittest.TestCase):
    """
        This test the case for maximum integer
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([20, 23, 12, 4]), 23)

    def test_max_float(self):
        self.assertEqual(max_integer([2.3, 4.6, 1.9, 0.8]), 4.6)

    def test_negative(self):
        self.assertEqual(max_integer([-1.4, -5.7, -6.99, -2.3]), -1.4)

    def test_single_int(self):
        self.assertIs(max_integer([1]), 1)

    def test_no_value(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        self.assertRaises(TypeError, max_integer, True)
