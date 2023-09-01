#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    value = urllib.parse.urlencode({"email": argv[2]}).encode("ascii")
    req = urllib.request.Request(argv[1], value)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))