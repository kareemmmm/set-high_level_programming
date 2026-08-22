#!/usr/bin/python3
"""Uses GitHub API with Basic Authentication to display user ID."""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    json_data = r.json()
    print(json_data.get("id"))
