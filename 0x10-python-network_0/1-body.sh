#!/bin/bash
#retrieve the body of the response
curl -sI "$1" | grep "Location:" | cut -d "/" -f 2
