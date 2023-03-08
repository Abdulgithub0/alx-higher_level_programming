#!/usr/bin/python3
second = 1
third = 1
for first in range(9):
    while second < 10:
        print('{}{}'.format(first, second), end='')
        if (first == 8 and second == 9):
            print()
        else:
            print(', ', end='')
        second += 1
    third += 1
    second = third
