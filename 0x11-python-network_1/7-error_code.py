#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""


import requests
import sys

def send_req(url):
    """
        sends request to url passed as a param and
        return an error

        Args:
            url: url to send req to
    """
    req = requests.get(url)
    if req.status_code > 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)


if __name__ == "__main__":
    url = sys.argv[1]
    send_req(url)
