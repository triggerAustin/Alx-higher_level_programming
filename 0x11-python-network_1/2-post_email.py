#!/usr/bin/python3
"""
takes in a URL and an email,
sends a POST request to the passed URL with the email as a paramete
displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
