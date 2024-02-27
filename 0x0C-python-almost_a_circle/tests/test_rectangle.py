#!/usr/bin/python3
"""Import all necessaries liabrary"""

from models.rectangle import Rectangle
import json
import unittest
from io impoet StringIO
import sys


class Testcode(unittest.TestCase):
    """
        Class test of square, Rectangle and the base
    """

    def setUp(self):
        """
            Run code before every single test
            once before anything
        """
        Base.Base__nb__objects = 0

    def test_rec1(self):
        """Test all attrs"""
        r1 = Rectangle(10, 2, 1, 2, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 12)

    def test_rec2(self):
        """Test all attrs"""
        r1 = Rectangle(4, 3, 1, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_inheritance(self):
        """Test the class inherited from"""
        r1 = Rectangle(1, 1)
        self.assertIsInstance(r1, Base)

    def test_arg_error(self):
        """Test error raised by with 0 and 1 arg passed"""
        with self.assertRaises(TypeError):
            new = Rectangle(0)
        with self.assertRaises(TypeError):
            new = Rectangle(3)

    def test_setter(self):
        """Test change of attrs"""
        rec = Rectangle(2, 3, 1, 0)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        rec.width = 7
        rec.height = 3
        self.assertEqual(rec.width, 7)
        self.assertEqual(rec.height, 3)

    def test_attr(self):
        """Test attrs passed"""
        with self.assertRaises(TypeError):
            new = Rectangle("H", 3, 1, 0)
        with self.assertRaises(TypeError):
            new = Rectangle(10, "3", 1, 0)
        with self.assertRaises(TypeError):
            new = Rectangle(12, 3, "1", 0)
        with self.assertRaises(TypeError):
            new = Rectangle(5, 3, 1, "5")

    def test_setter2(self):
        """Test error raised by passing 0 and negative"""
        rec = Rectangle(4, 9, 1, 0)
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 9)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 0)
        with self.assertRaises(ValueError):
            rec.height = 0
        with self.assertRaises(ValueError):
            rec.width = 0
        with self.assertRaises(ValueError):
            rec.height = -33
        with self.assertRaises(ValueError):
            rec.width = -45
        with self.assertRaises(ValueError):
            rec.x = -1
        with self.assertRaises(ValueError):
            rec.y = -4

    def test_setter3(self):
        """Test Error raise by Type"""
        rec = Rectangle(22, 45, 3, 6)
        self.assertEqual(rec.width, 22)
        self.assertEqual(rec.height, 45)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 6)
        with self.assertRaises(TypeError):
            rec.height = 'good'
        with self.assertRaises(TypeError):
            rec.width = "hello world"
        with self.assertRaises(TypeError):
            rec.x = "size"
        with self.assertRaises(TypeError):
            rec.y = "long"
        with self.assertRaises(TypeError):
            rec.height = 34.6
        with self.assertRaises(TypeError):
            rec.width = 12.0
        with self.assertRaises(TypeError):
            rec.x = 2.3
        with self.assertRaises(TypeError):
            rec.y = 5.7
        with self.assertRaises(TypeError):
            rec.height = [3, "H"]
        with self.assertRaises(TypeError):
            rec.y = {"key": "value"}

    def test_area(self):
        """Test Area of Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r1.width = 7
        r1.height = 3
        self.assertEqual(r1.area(), 21)
        r2 = Rectangle(16, 3, 2, 3)
        self.assertEqual(r2.area(), 48)
        r2.width = 5
        r2.height = 10
        self.assertEqual(r2.area(), 50)
        with self.assertRaises(TypeError):
            r2.area(3)

    def test_access(self):
        """Test error raised by accessing private attrs"""
        new = Rectangle(4, 5, 2, 6)
        with self.assertRaises(AttributeError):
            new.__height
        with self.assertRaises(AttributeError):
            new.__width
        with self.assertRaises(AttributeError):
            new.__x
        with self.assertRaises(AttributeError):
            new.__y
        with self.assertRaises(AttributeError):
            new.__id

    def test_display1(self):
        """Test output method without x and y"""
        new = Rectangle(4, 2, 0, 0)
        result = "####\n####\n"
        # We capture the printed output to
        # compare it with the expected result
        captured_output = StringIO()
        sys.stdout = captured_output
        new.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), result)
        """Test with x and y"""
        new2 = Rectangle(2, 3, 1, 1)
        result = "\n ##\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        new2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), result)

    def test_print_str(self):
        """Test the output method"""
        new = Rectangle(2, 3, 1, 1)
        self.assertEqual("[Rectangle] (11) 1/1 - 2/3", new.__str__())
        new.height = 4
        new.width = 6
        self.assertEqual("[Rectangle] (11) 1/1 - 6/4", new.__str__())


if __name__ == '__main__':
    unittest.main()
