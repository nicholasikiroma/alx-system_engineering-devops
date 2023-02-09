#!/usr/bin/python3
"""Python script returns information about TODO list progress for users."""
import requests
import sys


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
    if user:
        tasks = fetch_todo(user_id)
        completed_tasks = tuple(filter(lambda x: x['completed'],
                                       tasks))
        name = user.get('name')
        print("Employee {} is done with tasks({}/{}):".format(
            name, len(completed_tasks), len(tasks)))
        for title in completed_tasks:
            print('\t', title['title'])

    else:
        return


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        print_data(user_id)
    except Exception as err:
        print(err)
