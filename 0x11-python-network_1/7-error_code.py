#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response  (decoded in utf-8)
"""
import requests
from sys import argv


def browser(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        print(resp.text)
    except requests.exceptions.RequestException:
        print("Error code:", resp.status_code)


if __name__ == "__main__":
    browser(argv[1])
