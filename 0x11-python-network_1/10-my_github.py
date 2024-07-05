#!/usr/bin/python3

import request
import sys
from requests.auth import HTTPBasicAuth

if __name__ = "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, password)
    response = request.get(url, auth=auth)
    print(response.json().get("id))
