#!/usr/bin/ptyhon3

import requests
import sys

if __name__ == "__main__":
    url = 'https://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        parsed_response = response.json()
        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get("id"), parsed_response.get("name")))
    except ValueError:
        print(:Not a valid JSON")
