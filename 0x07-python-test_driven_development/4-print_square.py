#!/usr/bin/python3
"""Function that output square of certain size"""


def print_square(size):
    """Definiing validation and computation

    Args:
        size: size of the square
    """
    if (type(size) == float):
        size = int(size)
    if (type(size) is not int):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError("size must be >= 0")
    [print('#' * size) for i in range(size)]
