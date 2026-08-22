#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter parameter."""
import sys
import requests

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
