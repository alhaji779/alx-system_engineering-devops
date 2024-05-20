#!/usr/bin/python3
""" Script to copy api response to file
"""
import json
import requests
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(u)
    users = requests.get(url).json()
    user_name = users.get("username")
    todos = requests.get(url + '/todos').json()

    data_dict = {u: []}
    for t in todos:
        t_title = t.get("title")
        t_status = t.get("completed")
        data_dict[u].append({"task": "{}".format(t_title),
                            "completed": t_status,
                             "username": "{}".format(user_name)})

    with open("{}.json".format(u), "w") as json_file:
        json.dump(data_dict, json_file)
