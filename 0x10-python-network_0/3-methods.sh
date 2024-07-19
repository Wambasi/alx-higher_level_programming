#!/bin/bash
#bash script that takes in a URL and displays HTTP method the server accepts
curl -sI -X OPTIONS "$" | grep Allow | cut -c 8-
