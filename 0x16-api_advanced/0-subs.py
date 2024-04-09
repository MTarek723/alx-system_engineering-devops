#!/usr/bin/python3
"""contain subs function """

import requests


def number_of_subscribers(subreddit):
    """function to return number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit))
    r = r.json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
