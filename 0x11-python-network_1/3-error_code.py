#!/usr/bin/python3
"""This is a Python script that takes in a URL, sends a request to the URL, and
displays the body of the response (decoded in utf-8). It handles HTTP errors
and prints the error code if an HTTP error occurs."""

from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code "\n")
