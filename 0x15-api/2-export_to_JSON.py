#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys


def todo_list():
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    req = r.json()
    EMPLOYEE_NAME = req.get('username')
    user_id = req.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    req_todos = r.json()
    TASK_TITLE = []
    completed = []
    for index in req_todos:
        if index.get('userId') == user_id:
            TASK_TITLE.append(index.get('title'))
            completed.append(index.get('completed'))
    lis = [{'username': EMPLOYEE_NAME, 'completed':
           completed[index], 'task': e} for index, e in enumerate(TASK_TITLE)]
    json_dict = {user_id: lis}
    with open('{}.json'.format(sys.argv[1]), mode='w') as json_file:
        json.dump({user_id: lis}, json_file)


if __name__ == "__main__":
    todo_list()
