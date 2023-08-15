#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status using urllib package only"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
