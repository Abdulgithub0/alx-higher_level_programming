#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests as req
    try:
        with req("https://alx-intranet.hbtn.io/status") as res:
            r = res.text
            print("Body response:")
            print("\t- type: {}".format(type(r)))
            print("\t- content: {}".format(r))
    except req.exceptions.RequestException as e:
        pass
