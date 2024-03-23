#!/usr/bin/python3
""" Script that fetches https://alu-intranet.hbtn.io/status """
import urllib.request

url = 'https://intranet.htbn.io/status'
if url.startswith('https://'):
    url = "https://alu-intranet.htbn.io/status"

if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
