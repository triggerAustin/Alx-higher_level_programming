#!/bin/bash

# check if url is passed as arg
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

# send request using curl to url

curl -s -o /dev/null -w '%{size_download}\n' "$URL"
