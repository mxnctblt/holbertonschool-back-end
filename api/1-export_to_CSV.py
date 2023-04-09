#!/usr/bin/python3
# task 1
""" Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = get(url + "users/{}".format(argv[1])).json()
    username = employee.get("username")
    total = get(url + "todos", params={"userId": argv[1]}).json()
    user_id = argv[1]

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in total:
            w.writerow([user_id, username, t.get("completed"),
                        t.get("title")])
