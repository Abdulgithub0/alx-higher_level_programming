#!/usr/bin/python3


"""implementing unittest cases for Class Base"""


import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """defining unittest method for 
        each base class edge cases
    """

    def testNone_id(self):
        """test for empty instances
        initialization with empty id value
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def testMixed_id(self):
        """for both empty and non-empty instance declaration"""
        b3 = Base(12)
        b4 = Base()
        self.assertNotEqual(b3.id, b4.id)

    def testId_setter(self):
        """test for setter method"""
        b5 = Base()
        b5.id = 10
        self.assertEqual(b5.id, 10)

    def testid_getter(self):
        """test for getter method of the attr id"""
        b6 = Base()
        get = b6.id
        self.assertEqual(get, 5)

if __name__ == '__main__':
    unittest.main()
