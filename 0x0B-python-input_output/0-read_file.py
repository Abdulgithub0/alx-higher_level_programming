#!/usr/bin/python3
"""function that read text file """


def read_file(filename=""):
    """function definition

    Args:
        filename (str): location or naame of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        string = f.read()
        print(string, end='')
