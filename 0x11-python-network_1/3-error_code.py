#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib import request, parse, error
    from sys import argv

    def browser(url):
        try:
            with request.urlopen(url) as resp:
                recv = resp.read()
                print(recv.decode("utf-8"))
        except error.HTTPError as err:
            print("Error code:", err.code)
    browser(argv[1])
