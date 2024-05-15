#!/bin/bash
# Script that sends a POST request and displays the body response
curl -s -X "POST" -d "email=test@gmail.com" -d "subject=I will always be there for PLD" "$1"
