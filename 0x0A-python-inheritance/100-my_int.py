#!/usr/bin/python3
"""MyInt class inherit from int"""


class MyInt(int):
    """implementing MyInt class"""

    def __eq__(self, other):
        if (super().__eq__(other) == True):
            return False
        else:
            return True

    def __ne__(self, other):
        if (super().__ne__(other) == True):
            return False
        return True
