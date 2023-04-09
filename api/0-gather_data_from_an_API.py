#!/usr/bin/python3
# task 0
""" script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.

Requirements:
    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list
    progress in this exact format:
        - First line: Employee EMPLOYEE_NAME is done with tasks
          (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
              of completed and non-completed tasks
        - Second and N next lines display the title of completed tasks:
          TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = get(url + "users/{}".format(argv[1])).json()
    total = get(url + "todos", params={"userId": argv[1]}).json()

    completed = [task.get("title") for task in total
                 if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(total)))
    for c in completed:
        print("\t {}".format(c))
