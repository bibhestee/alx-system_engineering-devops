#!/usr/bin/python3
"""
    Gather data from an API
"""

import requests
import sys

id = sys.argv[1]

url = "https://jsonplaceholder.typicode.com"\
      "/users/{}/todos/".format(id)
url_2 = "https://jsonplaceholder.typicode.com"\
        "/users/{}".format(id)

response = requests.get(url)
response_2 = requests.get(url_2)

tasks = response.json()
details = response_2.json()

if __name__ == "__main__":
    user = details.get('name')
    total_task = len(tasks)
    done_task = 0
    titles = []
    for task in tasks:
        if task.get('completed') is True:
            titles.append(task.get('title'))
            done_task += 1
    output = "Employee {} is done with tasks({}/"\
        "{}):".format(user, done_task, total_task)
    print(output)
    for title in titles:
        print('\t ' + title)
