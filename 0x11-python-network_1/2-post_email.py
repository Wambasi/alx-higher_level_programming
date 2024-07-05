#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email =sys.argv[2]
    data = {'email': email}
    data_encoded = urllib.parse.urlencode(data).encode('ascii')
    with urllib.request.urlopen(url, data=data_encoded) as response:
        body = response.read().decode('utf-8')
        print(body)
