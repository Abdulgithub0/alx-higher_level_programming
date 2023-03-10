#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argv_lenght = len(argv)
    operators = ["+", "-", "*", "/"]
    if (argv_lenght != 4):
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    elif (argv[2] not in operators):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        cast_arg1 = int(argv[1])
        cast_arg3 = int(argv[3])
        if (argv[2] == operators[0]):
            result = add(cast_arg1, cast_arg3)
        elif (argv[2] == operators[1]):
            result = sub(cast_arg1, cast_arg3)
        elif (argv[2] == operators[2]):
            result = mul(cast_arg1, cast_arg3)
        else:
            result = div(cast_arg1, cast_arg3)
    print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], result))
