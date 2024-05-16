#!/usr/bin/python3
"""
A script that takes a letter,
sends a POST request to http://0.0.0.0:5000/search_user,
and displays the id and namefrom the response if it's valid JSON.
Uses the requests package and adheres to the specified constraints.
"""

import sys
import requests


def search_api(letter):
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    try:
        req = requests.post(url, data=payload)
        json_req = req.json()
        if json_req:
            print("[{}] {}".format(json_req.get('id'),
                                   json_req.get('name')))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        char = sys.argv[1]
    else:
        char = ""

    search_api(char)
