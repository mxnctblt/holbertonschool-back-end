#!/usr/bin/python3
# task 2
""" Using what you did in the task #0, extend your Python script to export data
in the JSON format.

Requirements:
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS,
                     "username": "USERNAME"},
                        {"task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS,
                     "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = get(url + "users/{}".format(argv[1])).json()
    username = employee.get("username")
    total = get(url + "todos", params={"userId": argv[1]}).json()
    user_id = argv[1]

    with open("{}.json".format(user_id), "w") as jsonfile:
        for t in total:
            json.dump({user_id: {"task": t.get("title"),
                                 "completed": t.get("completed"),
                                 "username": username}}, jsonfile)
