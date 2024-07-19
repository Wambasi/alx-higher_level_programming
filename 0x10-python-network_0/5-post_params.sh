#!/bin/bash
#script that takes in URL and sends a POST request to passed URL then displays body response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
