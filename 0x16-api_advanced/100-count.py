#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces) """
    global after
    global count_dic
    headers = {'User-Agent': '5ara/v1.0.0 (by /u/Tefa_23)'}
    id = 'Iveor9egCPolZahGK0MPpQ'
    passw = 'vgxoTcT2eVMFL7THy77MW786eGYAYQ'
    auth = requests.auth.HTTPBasicAuth(id, passw)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                          auth=auth,  params=parameters)
