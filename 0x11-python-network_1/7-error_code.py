#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response  (decoded in utf-8)
"""
import requests
from sys import argv


def browser(url):
    try:
        with requests.get(url) as resp:
            print(recv.text)
    except request.exceptions.RequestException:
        print("Error code:", resp.raise_for_status())


if __name__ == "__main__":
    browser(argv[1])
