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
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com"\
          "/todos"
    url_2 = "https://jsonplaceholder.typicode.com"\
            "/users"

    response = requests.get(url)
    response_2 = requests.get(url_2)

    tasks = response.json()
    details = response_2.json()

    file_path = 'todo_all_employees.json'

    data = {}
    for user in details:
        id = user.get('id')
        u = user.get('username')
        todo = []
        for task in tasks:
            uid = task.get('userId')
            c = task.get('completed')
            t = task.get('title')
            if id == uid:
                todo.append({"username": u, "task": t,
                            "completed": c})
        data[id] = todo

    with open(file_path, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    api_data()
