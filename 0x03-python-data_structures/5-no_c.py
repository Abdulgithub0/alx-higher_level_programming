#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for letter in my_string:
        if ord(letter) != 99 and ord(letter) != 67:
            new_string += letter
    return (new_string)
