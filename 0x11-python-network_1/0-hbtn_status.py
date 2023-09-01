#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request as req
    try:
        with req.urlopen("https://alx-intranet.hbtn.io/status") as res:
            r = res.read()
            print("Body response:")
            print("\t- type: {}".format(type(r)))
            print("\t- content: {}".format(r))
            print("\t- utf-8 content: {}".format(r.decode("utf-8")))
    except req.URLError as e:
        pass
