#!/usr/bin/python3
"""
    The script return the value of X-Request-Id
    found in the response header from server
"""

import requests as req
from sys import argv


def browser(url):
    try:
        with req.get(url) as resp:
            print(resp.headers.get("X-Request-Id"))
    except req.exceptions.RequestException as e:
        pass


if __name__ == "__main__":
    browser(argv[1])
