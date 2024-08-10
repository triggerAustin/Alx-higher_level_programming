#!/usr/bin/python3
"""
"""

import sys
import requests

def fetch_res_email(url):
    """
    """
    email = sys.argv[2]
    res = request.get(url, params=email)
    print(res.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_res_email(url)
