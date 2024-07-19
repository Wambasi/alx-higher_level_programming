#!/bin/bash
#script that sendsa JSON POST request to a URL as the first arguement, displays body response
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
