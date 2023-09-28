#!/bin/bash
# This script sends a request to a URL using curl and displays the size of the response body in bytes

# Check if an argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a request to the URL and capture the response body size in bytes
response_size=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}')

# Check if the response size is empty (no Content-Length header)
if [ -z "$response_size" ]; then
    echo "Unable to determine the response size."
else
    echo "Response Size: ${response_size} bytes"
fi
