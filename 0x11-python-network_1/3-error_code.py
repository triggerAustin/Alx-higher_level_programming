#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL,
and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error Code:", e.code)
