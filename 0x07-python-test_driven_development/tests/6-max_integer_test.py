#!/usr/bin/python3
"""unit test for the function max_integer()"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list1(self):
        """ sorted list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, msg="Incorrect!")

    def test_list2(self):
        """test for unsorted list elements"""
        self.assertEqual(max_integer([10, 8, 3, 9, 1, 6, 4, 5, 2]), 10, msg='Incorrect!')

    def test_emptylist(self):
        self.assertIsNone(max_integer([]), msg="Incorrect!")

    def test_for_strings(self):
        self.assertEqual(max_integer(["Alpha", "Beta", "Comma", "Gammma", "abdul is the king"]), "abdul is the king")

    def test_for_char(self):
        self.assertEqual(max_integer("Alx africa"), "x")

    def test_for_single(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer("A"), "A")
        self.assertEqual(max_integer(['b']), 'b')

    def test_for_float_list(self):
        self.assertEqual(max_integer([1.1, 2.1, 3.2, 4.3, 5.4, 20.0, 19.9]), 20.0)


if __name__ == '__main__':
    unittest.main()
