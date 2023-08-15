#!/usr/bin/python3

"""This is a script that:
-  use the packages 'urllib' and 'sys' only
- takes in a URL,
- sends a request to the URL
- displays the value of the X-Request-Id variable
  found in the header of the response.
"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
