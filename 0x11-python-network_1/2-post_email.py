#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    def browser(url, mail):
        try:
            d = {"email": mail}
            mail = parse.urlencode(d).encode("ascii")
            with request.urlopen(url, mail) as resp:
                recv = resp.read()
                print(recv.decode("utf-8"))
        except Exception as e:
            return
    browser(argv[1], argv[2])
