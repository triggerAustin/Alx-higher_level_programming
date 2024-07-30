#!/bin/bash
# check if url is passed as arg
curl -s -o /dev/null -w '%{size_download}\n' "$1"
