#!/bin/bash
# Fetch and print body size in bytes from given URL
curl -s -o /dev/null -w "%{size_download}\n" "$1"
