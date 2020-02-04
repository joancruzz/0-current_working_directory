#!/usr/bin/python3
"""Export data in the CSV forat"""
import csv
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
    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        write = csv.writer(csv_file, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for i, x in enumerate(TASK_TITLE):
            write.writerow([user_id, EMPLOYEE_NAME, completed[i], x])


if __name__ == "__main__":
    todo_list()
