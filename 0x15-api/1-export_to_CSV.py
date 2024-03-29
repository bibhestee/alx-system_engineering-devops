#!/usr/bin/python3
"""
    Gather data from an API

    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""


def api_data():
    """a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress."""

    import csv
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

    user = details.get('username')
    u_id = details.get('id')
    file_path = '{}.csv'.format(u_id)

    with open(file_path, 'w') as f:
        file = csv.writer(f, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            u = task.get('userId')
            c = task.get('completed')
            t = task.get('title')
            file.writerow([u, user, c, t])


if __name__ == "__main__":
    api_data()
