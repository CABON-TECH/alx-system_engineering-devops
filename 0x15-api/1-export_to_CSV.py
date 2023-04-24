#!/usr/bin/python3
"""
This script writes data from an API to a csv file
"""
import csv
import requests
import sys
if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/',
                        params={'userId': sys.argv[1]}).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    userid = sys.argv[1]
    username = user.get('username')

    with open("{}.csv".format(userid), "w", newline="") as csvfile:
        file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [file_writer.writerow(
            [userid, username, task.get('completed'), task.get('title')]
        )for task in todo]
