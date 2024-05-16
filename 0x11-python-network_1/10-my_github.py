#!/usr/bin/python3
"""
    Fetch ID from Github using
    GitHub credentials (username and password)
    Using Basic Authentication
"""
import sys
import requests


if __name__ == "__main__":
    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user',
                     auth=basic)
    if r.json() == {}:
        print("None")
    else:
        print("{}".format(r.json().get('id')))
