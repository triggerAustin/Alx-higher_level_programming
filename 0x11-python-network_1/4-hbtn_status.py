#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __main__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    res_txt = res.text
    print("Body response:")
    print("\t- type:", type(res_txt))
    print("\t- content:", res_txt)
    print(req)
