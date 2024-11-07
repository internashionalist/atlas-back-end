#!/usr/bin/python3
"""
This module fetches data from an API.
"""
import requests
import sys


def fetch_employee_progress(employee_id):
    """
    Fetches to-do progress of an employee by ID
    """
    # urls with data to be fetched
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todo_url = f"{base_url}todos?userId={employee_id}"

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # check for valid responses
    if todo_response.status_code != 200:
        print(f"To-Do List Fetch Fail: {employee_id}")
        return
    if user_response.status_code != 200:
        print(f"Name Fetch Fail: {employee_id}")
        return
