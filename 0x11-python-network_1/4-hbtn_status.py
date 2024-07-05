#!/usr/bin/python3

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = request.get(url)
    data = response.text
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
