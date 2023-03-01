#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns top 10 posts"""
    payload = {
        "after": after
    }
    url = 'https://www.reddit.com/r/{}/hot.json'.format(
        subreddit)
    req = requests.get(
        url, headers={'User-Agent': 'Python/requests'}, data=payload)
    try:
        subreddit_data = req.json()
        posts = subreddit_data.get('data', {}).get('children', None)
        after = subreddit_data.get('data', {}).get('after', None)

        if posts is not None:
            for post in posts:
                hot_list.append(post.get('data').get('title'))

        if after is None:
            if len(hot_list) == 0:
                return None
            return hot_list
        else:
            return recurse(subreddit, hot_list, after=after)
    except Exception:
        return None
