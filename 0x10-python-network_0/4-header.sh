#!/bin/bash
#bash script that takes in URL arguements and sends a GET request to the URL, sends body response
curl -s -H "X-School-User-Id: 98" "$1"
