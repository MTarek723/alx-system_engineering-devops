#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        for user in users:
            todos = requests.get(
                url + "todos", params={"userId": user["id"]}).json()
            for t in todos:
                jsonfile.write(
                    json.dumps(
                        {user["id"]: [{
                            "username": t["title"],
                            "task": t["title"],
                            "completed": t["completed"]
                        }]}
                    )
                )
