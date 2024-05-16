#!/usr/bin/python3
"""
    Write a Python script that takes in a URL
    sends a request to the URL and
    displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code < 400:
        print("{}".format(req.text))
    else:
        print(f'Error code: {req.status_code}')
