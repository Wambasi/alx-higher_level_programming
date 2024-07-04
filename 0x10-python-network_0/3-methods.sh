#!/bin/bash

curl -sI -X OPTIONS "$" | grep Allow | cut -c 8-
