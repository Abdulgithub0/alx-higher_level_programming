#!/usr/bin/python3
def islower(c):
    if (c >= 'a' and c <= 'z'):
        return (True)
    return (False)

if __name__ == '__main__':
    import sys
    print(islower(sys.argv[1]))
