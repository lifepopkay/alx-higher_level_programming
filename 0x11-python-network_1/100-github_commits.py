#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""

import requests
from sys import argv


def fetch_users(repo_name, acct_name):
    url = f'https://api.github.com/repos/{repo_name}/{acct_name}/commits'
    r = requests.get(url)
    r_json = r.json()
    
    # Get the first 10 commits
    count = 1
    for commit in r_json:
        if count < 11:
            count += 1
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

if __name__ == "__main__":
    fetch_users(argv[1], argv[2])
