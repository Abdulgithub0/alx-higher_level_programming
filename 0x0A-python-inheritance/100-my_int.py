#!/usr/bin/python3
"""MyInt class inherit from int"""


class MyInt(int):
    """implementing MyInt class"""

    def __eq__(self, other):
        if (super().__eq__(other)):
            return False
        else:
            return True

    def __ne__(self, other):
        if (super().__ne__(other)):
            return False
        return True
