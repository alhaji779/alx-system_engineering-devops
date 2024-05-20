#!/usr/bin/python3
""" A python script to fetch data from API
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url+'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url+'todos/?userId={}'.format(sys.argv[1]))
    todo_all = todos.json()
    completed = []
    for todo in todo_all:
        if todo.get("completed") is True:
            completed.append(todo)

    print("Employee {} is done with tasks({}/{}):".format(users.
          get("name"), len(completed), len(todo_all)))

    for t in completed:
        print("\t {}".format(t.get("title")))
