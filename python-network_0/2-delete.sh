#!/bin/bash
# This script takes a URL as an argument and sends a DELETE request to the server
curl -s -X DELETE "$1"
