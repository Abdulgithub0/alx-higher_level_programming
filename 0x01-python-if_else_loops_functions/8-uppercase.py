#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        let_char = letters
        if letters >= 'a' and letters <= 'z':
            let_char = chr(ord(letters) - 32)
        print('{}'.format(let_char), end='')
    print()
