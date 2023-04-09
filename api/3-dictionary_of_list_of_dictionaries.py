#!/usr/bin/python3
# task 3
""" Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME",
                    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
                    {"username": "USERNAME", "task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [
                    {"username": "USERNAME", "task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS},
                    {"username": "USERNAME", "task": "TASK_TITLE",
                    "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""
from requests import get
import json


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users = get(users_url).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        for u in users:
            todos = get(todos_url, params={"userId": u.get("id")}).json()
            for t in todos:
                json.dump({
                    u.get("id"): [{
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": u.get("username")
                    }]}, jsonfile)
