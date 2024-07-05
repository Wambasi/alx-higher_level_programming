#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = request.get(url)
    header_value = response.headers.get('X-Request-Id')
    print(header_value)
