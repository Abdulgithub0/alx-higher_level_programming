#!/usr/bin/python3
""" a Python script that takes your GitHub credentials
(username and password=personal access token) and uses
the GitHub API to display your id
"""
import requests as req
from requests.auth import HTTPBasicAuth
from sys import argv as credentials


def get_github_id(username, passwd):
    try:
        url = "https://api.github.com/user"
        response = req.get(url, auth=HTTPBasicAuth(username, passwd))
        response.raise_for_status()
    except (req.exceptions.RequestException, ValueError):
        pass
    finally:
        print(response.json().get("id"))


if __name__ == "__main__":
    get_github_id(credentials[1], credentials[2])
