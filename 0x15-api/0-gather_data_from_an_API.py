#!/usr/bin/python3
"""
This script gathers data from an API using urllib
It then serializes the json data to a python dictionary and prints it out
It takes an parameter, the user Id of the user's data that you want
"""
import requests
import sys
if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={'userId': sys.argv[1]}).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    completed = [task.get('title')
                 for task in todo if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    [print("\t {}".format(title)) for title in completed]
