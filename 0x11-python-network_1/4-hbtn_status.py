#!/usr/bin/python3
"""This is a Python script that
- fetches https://alx-intranet.hbtn.io/status
- use the package 'requests' only,
- displaying the body of the response in 'tabulation before -' format.
"""
import urllib.request
import urllib.error
import sys.argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as page:
            print(page.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
