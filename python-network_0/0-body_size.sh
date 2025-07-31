#!/bin/bash
# Use curl to fetch the body (-s for silent, -o to throw away output, -w for size)
curl -s -o /dev/null -w "%{size_download}\n" "$url"
