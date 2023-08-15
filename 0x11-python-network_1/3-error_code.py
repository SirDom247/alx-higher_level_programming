#!/usr/bin/python3
"""This is Python script that takes in a URLand an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""

from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
        try:
            with request.urlopen(argv[1]) as page:
                print(page.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))

