#!/bin/bash
# Displays only the HTTP status code without using pipes, redirections, ;, or &&
curl -s -o /dev/null -w "%{http_code}" "$1"
