#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_init(unittest.TestCase):
    """test for Base class __init__"""

    def testNone_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id, msg='check testNone_id')

    def testMixed_id(self):
        b3 = Base(12)
        b4 = Base()
        self.assertNotEqual(b3.id, b4.id, msg='check testMixed_id')

    def testId_setter(self):
        b5 = Base()
        b5.id = 10
        self.assertEqual(b5.id, 10, msg='testId_setter')

if __name__ == '__main__':
    unittest.main()
