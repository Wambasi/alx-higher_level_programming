#!/usr/bin/python3

import requests
import json

response = requests.fet('https://www.tutorialspoint.com/http/http_methods.htm')
print(response.json())
