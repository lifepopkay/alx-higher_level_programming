#!/usr/bin/python3
"""
    Script that takes in a URL and an email sends a POST request to that URL
    with the email as a parameter.
    Displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    mail = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=mail)
    print("{}".format(req.text))
