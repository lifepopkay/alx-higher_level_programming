import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class Testcode(unittest.TestCase):
    """
        Class test of square, rectangle and the base
    """

    def setUp(self):
        """
            Run code before every signle test
            once before anything
        """
        Base.Base__nb__objects = 0

    def test_squ1(self):
        """Test all attrs"""
        s1 = Square(4, 2, 2, 1)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 1)

    def test_inheritance(self):
        """Test the class inherited from"""
        r1 = Square(1)
        self.assertIsInstance(r1, Rectangle)

    def test_arg_error(self):
        """Test error raised by with 0 arg passed"""
        with self.assertRaises(TypeError):
            new = Square()

    def test_setter(self):
        """Test change of attrs"""
        s1 = Square(5, 2, 2)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        s1.size = 7
        s1.x = 3
        s1.y = 1
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 3)


if __name__ == '__main__':
    unittest.main()
