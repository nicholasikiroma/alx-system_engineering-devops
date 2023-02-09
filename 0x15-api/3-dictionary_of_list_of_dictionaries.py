#!/usr/bin/python3
"""Python script returns dictionary of all users"""
import requests
import json


def fetch_user():
    """Retrieves users from api"""
    base_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(base_url)
    return r.json()


def fetch_todo(user_id: str):
    """Retrieves user from api"""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'.format(
        user_id)
    r = requests.get(base_url)
    return r.json()


def user_and_todos(user: dict):
    """Link a user with his todos"""
    if user == {}:
        return
    userId = user.get("id")
    username = user.get("username")
    todos = fetch_todo(userId)
    tasks = list(map(
        lambda t: {
            "username": username,
            "task": t.get("title"),
            "completed": t.get("completed")},
        todos
    ))
    result = {userId: tasks}
    return result


def export_all():
    """Save all users with their tasks in a json format"""
    result = {}
    for user in fetch_user():
        result.update(user_and_todos(user))
    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(result))


if __name__ == "__main__":
    try:
        export_all()
    except Exception as err:
        print(err)
