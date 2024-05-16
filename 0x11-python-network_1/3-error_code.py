#!/usr/bin/python3
"""
    A script that takes in a URL and sends a request to the URL
    and displays the body of the response decoded in utf-8.
    urllib.error.HTTPError is managed and printed in the form
    Error code: <HTTP status code>
"""

import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
