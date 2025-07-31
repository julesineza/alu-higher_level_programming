#!/bin/bash
# Fetch and print body size in bytes from given URL
curl -s "$1" | wc -c
