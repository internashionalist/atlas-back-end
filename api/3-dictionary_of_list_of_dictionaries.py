#!/usr/bin/python3
"""
This module fetches data from an API and exports all
employees' to-do progress to a JSON file.
"""
import json
import requests
import sys


def fetch_employee_progress():
    """
    Fetches to-do progress of an employee by ID
    """
    # removed employee_id parameter

    # urls with data to be fetched
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    # fetch to-do list data
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"To-Do List Fetch Fail: {employee_id}")
        return
    todo_data = todo_response.json()

    # fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Name Fetch Fail: {employee_id}")
        return
    user_data = user_response.json()

    # create dictionary of all employees' tasks by ID
    tasks_list = []

    # map IDs to usernames for reference
    user_map = {user["id"]: user["username"] for user in user_data}

    # fetch task data for each employee
    for task in todo_data:
        user_id = task.get("userId")
        task_info = {
            "username": user_map.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        }

        if user_id not in tasks_list:
            tasks_list[user_id] = []
        tasks_list[user_id].append(task_info)

    # export data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as file:
        json.dump(tasks_list, file)

    # nice little message on completion
    print(f"All employees' tasks have been exported to {json_filename}.")


if __name__ == "__main__":
    fetch_employee_progress()
