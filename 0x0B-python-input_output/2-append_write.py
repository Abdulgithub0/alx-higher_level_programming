#!/usr/bin/python3
"""function that append text to a file """


def append_write(filename="", text=""):
    """function definition

    Args:
        filename (str): location or naame of the file to append txt into
        text: string of characters to be written into a filename
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
