#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import requests
from sys import argv


def browser(url, mail):
    try:
        d = {"email": mail}
        with requests.post(url, data=d) as resp:
            print(resp.text)
    except requests.exception.RequestException as e:
        return


if __name__ == "__main__":
    browser(argv[1], argv[2])
