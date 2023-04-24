#!/usr/bin/python3
"""
This script writes data from an API to a json file
"""

import json
import requests
import sys

if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={'userId': sys.argv[1]}).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    userid = sys.argv[1]
    username = user.get('username')
    data = {userid: [{
        "task": task.get('title'),
        "completed": task.get("completed"),
        "username": username
    } for task in todo]}
    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump(data, jsonfile)
