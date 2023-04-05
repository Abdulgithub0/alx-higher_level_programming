#!/usr/bin/python3
"""Function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """defining the function

    Args:
        text (string): text to be work upon and printed
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ('.', ':', '?'):
            print(text[i])
            print()
        else:
            if (text[i] == ' ' and text[i - 1] in ('.', ':', '?')):
                pass
            else:
                print(text[i], end='')
