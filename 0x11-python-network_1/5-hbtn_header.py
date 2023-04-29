#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url_input = sys.argv[1]

    req = requests.get(url_input)
    print(req.headers.get("X-Request-Id"))
