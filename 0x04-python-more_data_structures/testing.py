#!/usr/bin/python3
def username(param):
    new_str = param[0]
    count = 1
    for i in param:
        if (i == ' '):
            new_str = new_str + str(param[count])
        count += 1 
    return new_str


