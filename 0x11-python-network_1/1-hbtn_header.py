#!/usr/bin/python3
""" Import neccessary libraries """

import urllib.request
import sys
"""
    Send a request and fetch the value of 
    X-Request-Id
"""


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    html = response.info()
    header = html.get('X-Request-Id')
    print("{}".format(header))
