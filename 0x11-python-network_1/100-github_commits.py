#!/usr/bin/python3
"""
a Python script that takes 2 arguments and list 10 commits
(from the most recent to oldest) of the github repository
“rails” by the user “rails”
"""
import requests as req
from sys import argv


def latest_commits(repos, username):
    url = "https://api.github.com/repos/{}/{}/commits".format(
          repos, username)
    resp = req.get(url, params={"per_page": 10})
    try:
        json_data = resp.json()
        for data in json_data:
            s = data["sha"]
            name = data.get("commit").get("author").get("name")
            print(f"{s}: {name}")
    except KeyError as e:
        print(e)
if __name__ == "__main__":
    latest_commits(argv[1], argv[2])
