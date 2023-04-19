#!usr/bin/python3

"""implementing unittest for class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defining test methods for diff edge cases"""

    def testInheritId(self):
        """test for inherited id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 6)

    def test_Initializer(self):
        """testing for initializer method"""
        r2 = Rectangle(2, 10, 5, 6, 100)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 100)
