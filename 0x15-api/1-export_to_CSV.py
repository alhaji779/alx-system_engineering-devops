#!/usr/bin/python3
""" Script to copy api response to file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(u)
    users = requests.get(url).json()
    user_name = users.get("username")
    todos = requests.get(url + '/todos').json()

    with open("{}.csv".format(u), "w") as csv_file:
        for t in todos:
            t_status = t.get("completed")
            t_title = t.get("title")
            csv_file.write('"{}","{}","{}","{}"\n'.format(u,
                           user_name, t_status, t_title))
