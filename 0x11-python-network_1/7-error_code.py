#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
