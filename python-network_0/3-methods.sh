#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
