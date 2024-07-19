#!/bin/bash
#sends a requst to a URL as an arguement and displays the status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
