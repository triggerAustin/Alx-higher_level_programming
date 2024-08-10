#!/usr/bin/python3
"""
sends request to url with email as parameter
"""

import sys
import requests

def fetch_res_email(url):
    """
        makes request to the url

        Args:
            url: url to make request to
        Return:
            none
    """
    payload = {'email': sys.argv[2]}
    res = requests.post(url, data=payload)
    print(res.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_res_email(url)
