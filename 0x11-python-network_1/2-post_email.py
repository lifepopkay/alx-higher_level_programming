#!/usr/bin/python3
"""
    post an email
"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print('{}'.format(page))
