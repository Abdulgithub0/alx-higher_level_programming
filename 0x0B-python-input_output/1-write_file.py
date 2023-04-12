#!/usr/bin/python3
"""function that write text into a file """


def write_file(filename="", text=""):
    """function definition

    Args:
        filename (str): location or naame of the file to be read
        text: string of characters to be written into a filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
