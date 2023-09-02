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
    head_req = {"Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28"}
    resp = req.get(url, headers=head_req)
    json_data = resp.json()
    i = 0
    while(i < 10):

        print(json_data[i].get("sha") + ": ", end="")
        print(json_data[i].get("commit").get("author").get("name"))
        i = i + 1


if __name__ == "__main__":
    latest_commits(argv[1], argv[2])
