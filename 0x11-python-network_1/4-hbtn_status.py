#!/usr/bin/python3
"""
    This script fetches https://alx-intranet.hbtn.io/status using
    the requests package and displays the body of the response in
    a specified format.
"""

import requests


def fetch_res(url):
    """
        fetches https://alx-intranet.hbtn.io/status

        Args:
            url: to make request to
    """
    try:
        res = requests.get(url)
        res_txt = res.text
        print("Body response:")
        print("\t- type:", type(res_txt))
        print("\t- content:", res_txt)
    except requests.RequestException as e:
        print(f"Error fetching url: {e}")


if __main__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_res(url)
