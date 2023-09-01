#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(f'https://api.github.com/repos\
/{argv[2]}/{argv[1]}/commits')
    for count, r in enumerate(req.json()):
        if count == 10:
            break
        print(f"{r.get('sha')}:", r.get('commit').get('author').get('name'))