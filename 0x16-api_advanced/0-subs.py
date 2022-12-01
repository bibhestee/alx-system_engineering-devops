#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns the total
    number of subscriber for a subreddit.
"""


def number_of_subscribers(subreddit):
    """
    Number_of_subscribers: This function queries the Reddit API
    """

    import requests

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
