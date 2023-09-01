#!/usr/bin/python3
"""
    The script return the value of X-Request-Id
    found in the response header from server
"""
if __name__ == "__main__":
    import urllib.request as req
    from sys import argv

    def browser(url):
        try:
            with req.urlopen(url) as resp:
                print(resp.info().get("X-Request-Id"))
        except req.URLError as e:
            return
    browser(argv[1])
