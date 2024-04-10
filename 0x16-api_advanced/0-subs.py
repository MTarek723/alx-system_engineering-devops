#!/usr/bin/python3

""" Function that queries the Reddit API """

import requests
import sys
import time
import json


def number_of_subscribers(subreddit):
    """ Args:
    subreddit: subreddit name
    Returns:
    number of subscribers to the subreddit,
    or 0 if subreddit requested is invalid or if there is a JSONDecodeError"""

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    max_retries = 5  # Maximum number of retries
    retry_delay = 3  # Delay between retries in seconds

    for attempt in range(max_retries):
        try:
            response = requests.get(
                url, headers=headers, allow_redirects=False)
            response.raise_for_status()  # Raise error for non-2xx status codes
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response")
            if attempt == max_retries - 1:
                return 0
            time.sleep(retry_delay)  # Wait before retrying
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return 0
    return 0
