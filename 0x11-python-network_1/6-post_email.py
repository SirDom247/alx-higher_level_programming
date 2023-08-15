#!/usr/bin/python3
"""This is a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response.
It uses the packages 'requests' and 'sys' only.
"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.post(argv[1], resp={'email': argv[2]}).text)
