#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv


def search_user():
    url = "http://0.0.0.0:5000/search_user"
    arg = argv[1] if argv[1] else ""
    resp = requests.post(url, data={'q': arg})
    try:
        json_data = resp.json()
        if json_data and isinstance(json_data, list):
            print("[{}] {}".format(ele['id'], ele['name']))
        else:
            print("No result")
    except ValueError as err:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
