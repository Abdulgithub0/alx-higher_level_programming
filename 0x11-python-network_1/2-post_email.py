#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from urllib import request, parse
from sys import argv


def browser(url, mail):
    try:
        d = {"email": mail}
        mail = parse.urlencode(d).encode("utf-8")
        with request.urlopen(url, mail) as resp:
            recv = resp.read()
            print(recv.decode("utf-8"))
    except Exception as e:
        return


if __name__ == "__main__":
    browser(argv[1], argv[2])
