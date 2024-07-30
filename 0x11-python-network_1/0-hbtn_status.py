#!/usr/bin/python3
"""
Fetches data from https://alx-intranet.hbtn.io/status
Displays the type, content, and UTF-8 encoded content of the response.
"""
import urllib.request
import urllib.error

with urllib.request.urlopen(url) as response:
            content = response.read()
