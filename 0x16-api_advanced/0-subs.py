#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    id = 'Iveor9egCPolZahGK0MPpQ'
    passw = 'vgxoTcT2eVMFL7THy77MW786eGYAYQ'
    auth = requests.auth.HTTPBasicAuth(id, passw)
    headers = {
        'User-Agent': 'RedditAPIClient/1.0 (https://github.com/MTarek723)'
               }
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers=headers,
                     auth=auth).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
