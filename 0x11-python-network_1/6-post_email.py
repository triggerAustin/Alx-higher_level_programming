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
    email = sys.argv[2]
    res = requests.get(url, params=email)
    print(res.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_res_email(url)
