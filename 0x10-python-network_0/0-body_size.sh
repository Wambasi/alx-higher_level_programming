#!/bin/bash
#Takes in a url and sends a request to it and returns the number of bytes
curl -s "$1" | wc -c
