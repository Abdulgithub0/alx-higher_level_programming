#!/usr/bin/python3
"""Mylist class inherit from superclass list"""


class MyList(list):
    """subclass of list class with integrated sorted func"""
    def print_sorted(self):
        """print out a list obj in sorted order"""
        m_list = sorted(self)
        print(m_list)
