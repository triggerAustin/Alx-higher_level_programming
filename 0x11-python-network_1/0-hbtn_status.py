#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
displays body response
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = respones.read().decode('utf-8')

print("Body response:")
print(f"\t - type: {type(body)}")
print(f"\t - body: {body}")
print(f"\t - utf8 content: {body.encode('utf-8')}")
