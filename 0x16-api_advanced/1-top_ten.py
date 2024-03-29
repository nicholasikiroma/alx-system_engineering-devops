#!/usr/bin/python3
"""
Python script that
returns first 10
hot posts for
a given subreddit
"""
import requests


def top_ten(subreddit):
    """Returns top 10 posts"""
    try:
        url = 'https://www.reddit.com/r/{}/hot.json?'.format(
            subreddit)
        req = requests.get(url, headers={'User-Agent': 'Python/requests'})
        subreddit_data = req.json()
        num = 0
        while num < 10:
            post = subreddit_data['data']['children'][num]['data']['title']
            if post is None:
                print(None)
            print(post)
            num += 1

    except Exception:
        print(None)
