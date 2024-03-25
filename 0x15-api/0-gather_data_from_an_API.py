#!/usr/bin/python3
import json
import requests
from sys import argv

f1 = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
f1 = json.loads(f1.text)
EMPLOYEE_NAME = f1["name"]

f2 = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1]))
f2 = json.loads(f2.text)
NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
TASKS_DONE = []

for tasks in f2:
    if tasks["completed"] is True:
        NUMBER_OF_DONE_TASKS += 1
        TASKS_DONE.append(tasks["title"])
    TOTAL_NUMBER_OF_TASKS += 1

print("Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
for j in TASKS_DONE:
    print("\t{}".format(j))
