#!/usr/bin/python3
import json
import requests


def number_of_subscribers(subreddit):
    """ Args:
    subreddit: subreddit name
    Returns: number of subscribers, or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'ohmygodwhyitisnotworking'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return 0
    else:
        return 0
