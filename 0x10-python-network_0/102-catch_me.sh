#!/bin/bash
#script that makes a request to 0.0.0.0:5000/catch_me to the server returning a message
curl -sLX PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
