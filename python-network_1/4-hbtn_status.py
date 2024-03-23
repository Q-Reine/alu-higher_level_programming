#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = "https://alu-intranet.hbtn.io/status"

if __name__ == '__main__':
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
