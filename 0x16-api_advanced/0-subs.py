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

    try:
        r = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                         headers=headers,
                         auth=auth)
        r.raise_for_status()  # Raise an exception for non-2xx status codes
        subs = r.json().get("data", {}).get("subscribers", 0)
        return subs
    except requests.exceptions.RequestException:
        # Handle any exceptions that occur during the request
        return 0
