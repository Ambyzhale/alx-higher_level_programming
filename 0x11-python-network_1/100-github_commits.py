#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url_in = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url_in)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
