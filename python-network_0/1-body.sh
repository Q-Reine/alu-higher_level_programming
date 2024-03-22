#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
