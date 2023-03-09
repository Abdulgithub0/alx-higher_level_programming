#!/usr/bin/python3
from sys import argv
if (__name__ == '__main__'):
    num = len(argv)
    if (num == 1):
        print('{} arguments.'.format(0))
    elif (num == 2):
        print('{} argument:'.format(1))
        print('{}: {}'.format(1, argv[1]))
    else:
        print('{} arguments:'.format(num - 1))
        for i in range(1, num):
            print('{}: {}'.format(i, argv[i]))
