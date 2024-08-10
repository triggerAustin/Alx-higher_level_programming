#!/usr/bin/python3
"""
script takes in a URL and sends a request to it,
displays the variable x-Request-Id of the response
"""

import sys
import requests


def fetch_req_Id(url):
    """
        displays the x-request-Id of response

        Args:
            url: url to send req to
    """
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_req_id(url)
