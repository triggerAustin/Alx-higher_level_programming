#!/bin/bash
#sends a GET request to the URL,displays the body of the response
curl -s -w "%{http_code}" "$1"
