#!/usr/bin/python3
"""This is a Python script that
- fetches https://alx-intranet.hbtn.io/status
- use the package 'requests' only,
- displaying the body of the response in 'tabulation before -' format.
"""
import requests

if __name__ == "__main__":

    url = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(url.text.__class__))
    print("\t- content: {}".format(url.text))
