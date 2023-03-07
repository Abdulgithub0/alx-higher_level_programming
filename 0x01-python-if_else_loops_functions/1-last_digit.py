#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = 'Last digit of'
if number < 0:
    num = ((-1 * number) % 10)
    num = num * (-1)
else:
    num = number % 10
if num > 5:
    print(f'{string:s} {number:d} is {num} and is greater than 5')
elif num < 6 and num != 0:
    print(f'{string:s} {number:d} is {num} and is less than 6 and not 0')
else:
    print(f'{string:s} {number:d} is {num} and is 0')
