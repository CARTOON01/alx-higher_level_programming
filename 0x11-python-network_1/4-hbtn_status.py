#!/usr/bin/python3
"""
This script fetches "https://alx-intranet.hbtn.io/status"
"""
import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
value = r.content.decode('utf-8')
print('Body response:')
print(f"\t- type: {type(value)}")
print(f"\t- content: {value}")