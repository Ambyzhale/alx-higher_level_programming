#!/usr/bin/python3
"""A  script that:
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url_in = sys.argv[1]
    email= {"email": sys.argv[2]}

    r = requests.post(url_in, data=email)
    print(r.text)
