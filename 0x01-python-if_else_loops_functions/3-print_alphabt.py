#!/usr/bin/python3
for char in range(97, 123, 1):
    if char != 101 and char != 113:
        print("{:c}".format(char), end='')
