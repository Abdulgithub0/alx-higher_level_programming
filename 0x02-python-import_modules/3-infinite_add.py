#!/usr/bin/python3
from sys import argv
if (__name__ == '__main__'):
    num = len(argv)
    add = 0
    if (num > 2):
        for i in range(1, num):
            add += (int((argv[i])))
    elif (num == 2):
        add = int(argv[1])
    print('{}'.format(add))
