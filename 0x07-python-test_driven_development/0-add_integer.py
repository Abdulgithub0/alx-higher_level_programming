#!/usr/bin/python3
"""function that add two integer"""


def add_integer(a, b=98):
    """start of computation

        Args:
            a (int or float): value to be added to b.
            b (int or float): value to be added to a.

        Return: the result of the addition

        >>> add_integer(2, 3)
        5

        >>> add_integer('string', 6)
        Traceback (most recent call last):
        TypeError: a must be an integer

        >>> add_integer(8, 'string')
        Traceback (most recent call last):
        TypeError: b must be an integer
    """

    if (type(b) == float or type(a) == float):
        b = int(b)
        a = int(a)
    if not (isinstance(a, int)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int)):
        raise TypeError('b must be an integer')
    return (a + b)
