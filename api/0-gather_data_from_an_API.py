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
