#!/usr/bin/python3
"""Python script that returns number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns total no of subscribers"""
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        req = requests.get(url, headers={'User-Agent': 'Python/requests'})
        subreddit_data = req.json()
        no_subs = subreddit_data.get('data', {}).get('subscribers', 0)
        return no_subs

    except Exception:
        return 0
