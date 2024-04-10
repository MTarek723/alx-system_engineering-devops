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
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '5ara/v1.0.0 (by /u/Tefa_23)'},
                     auth=auth).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
