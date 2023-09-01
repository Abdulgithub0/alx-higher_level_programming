#!/usr/bin/python3
""" a Python script that takes your GitHub credentials
(username and password=personal access token) and uses
the GitHub API to display your id
"""
import requests as req
from sys import argv as credentials


def get_github_id(username, passwd):
    url = f"https://api.github.com/user?login={username}"
    auth = f"Bearer {passwd}"
    header = {"Authorization": auth,
              "Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28"}
    response = req.get(url, headers=header)
    response.raise_for_status()
    user_id = dict(response.json()).get("id")
    print(user_id)


if __name__ == "__main__":
    get_github_id(credentials[1], credentials[2])
