#!usr/bin/python3

"""implementing unittest for class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defining test methods for diff edge cases"""

    def test_initializer(self):
        """testing for initializer method"""
        r1 = Rectangle(2, 10, 5, 6, 100)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 100)

    def test_terror(self):
        """test for typeError"""
        with self.assertRaises(TypeError):
            r2 = Rectangle("5", 10, 2, 3, 1)

    def test_position_argument(self):
        """test for parameter overloading"""
        with self.assertRaises(TypeError):
            r3 =  Rectangle(5, 10, 2, 3, 1, 100)

    def test_empty_arg(self):
        """test for empty initialization"""
        with self.assertRaises(TypeError):
            r4 = Rectangle()
    def test_verror(self):
        """test for ValuError"""
        with self.assertRaises(ValueError):
            r4 = Rectangle(5, 10, 2, -3, 1)

if __name__ == '__main__':
    unittest.main()
