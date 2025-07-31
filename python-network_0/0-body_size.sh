#!/bin/bash
# Take the first argument as the URL
url="$1"

# Use curl to fetch the body (-s for silent, -o to throw away output, -w for size)
curl -s -o /dev/null -w "%{size_download}\n" "$url"
