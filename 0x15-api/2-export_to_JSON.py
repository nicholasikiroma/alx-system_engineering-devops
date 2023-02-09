#!/usr/bin/python3
"""Python script returns information about TODO list progress for users."""
import requests
import sys
import json


def fetch_user(user_id: str):
    """Retrieves users from api"""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    r = requests.get(base_url)
    return r.json()


def fetch_todo(user_id: str):
    """Retrieves user from api"""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'.format(
        user_id)
    r = requests.get(base_url)
    return r.json()


def print_data(user_id: str):
    """Prints formatted string representation of user data"""
    user = fetch_user(user_id)
    if user == {}:
        return
    username = user.get("username")
    todos = fetch_todo(user_id)
    tasks = list(map(
        lambda t: {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username},
        todos
    ))
    result = {user_id: tasks}
    with open("{}.json".format(user_id), "w") as f:
        f.write(json.dumps(result))


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        print_data(user_id)
    except Exception as err:
        print(err)
