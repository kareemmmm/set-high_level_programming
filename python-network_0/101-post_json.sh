#!/bin/bash
# Sends a JSON POST request with the content of a file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
