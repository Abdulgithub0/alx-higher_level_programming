#!/usr/bin/python3
for i in range(0, 99, 1):
    if i < 10:
        i = f'0{i}'
        i = int(i)
    print(f'{i:d}, ', end='')
print(99)
