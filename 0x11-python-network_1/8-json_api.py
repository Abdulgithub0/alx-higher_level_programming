#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv


def search_user(arg=""):
    url = "http://0.0.0.0:5000/search_user"
    resp = requests(url, data={'q': arg})
    try:
        json_data = resp.json()
        if json_data and isinstance(json_data, list):
            for ele in json_data:
                print("[{}] {}".format(ele.get('id'), ele.get('name')))
        else:
            print("No result")
    except ValueError as err:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user(argv[1])
