#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.

    Args:
        subreddit (str): The name of the subreddit to get subscriber count for.

    Returns:
        int: The number of subscribers for the given subreddit, or 0
    """
    # Set a custom User-Agent header to comply with Reddit API rules
    headers = {'User-Agent': 'my-reddit-app/0.1'}

    # Construct the API URL for the subreddit
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send a GET request to the API
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise error for non-2xx status codes

        # Parse the JSON response
        data = response.json()

        # Extract the subscriber count from the response data
        subscribers = data['data']['subscribers']

        return subscribers
    except (requests.exceptions.RequestException, KeyError):
        # Return 0 if an exception occurs (e.g., invalid subreddit, API error)
        return 0
