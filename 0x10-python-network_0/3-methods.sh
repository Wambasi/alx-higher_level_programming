#!/bin/bash
#bash script that takes in a URL and displays HTTP method the server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
