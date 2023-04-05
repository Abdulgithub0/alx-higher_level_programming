#!/usr/bin/python3
"""Function that print out first and last name"""


def say_my_name(first_name, last_name=""):
    """defining the function
    Args:
        first_name (str): refering to the person real name
        last_name (str): refering to the person family or father's name
    Return: Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
