#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def todo_list():
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    req = r.json()
    EMPLOYEE_NAME = req.get('name')
    user_id = req.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    req_todos = r.json()
    tasks, completed = 0, 0
    TASK_TITLE = []
    for index in req_todos:
        if index.get('userId') == user_id:
            tasks += 1
            if index.get('completed'):
                completed += 1
                TASK_TITLE.append(index.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, completed, tasks))
    for index in TASK_TITLE:
        print('\t', index)


if __name__ == "__main__":
    todo_list()
    import requests
    import sys
