#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ This function queries the Reddit API """

    url = f'https://www.reddit.com/r/{subreddit}.json'
    headers = {'User-Agent': 'MyServer/1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    try:
        result = response.json()['data']['children'][1]['data']
        return result.get('subreddit_subscribers')
    except IndexError:
        return 0
