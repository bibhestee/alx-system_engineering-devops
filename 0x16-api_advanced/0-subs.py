#!/usr/bin/python3
"""
    This module provides a function that sends a get request to the Reddit API
    with the specified subreddit then process the response to get the total
    number of subscriber for a subreddit.
"""


def number_of_subscribers(subreddit):
    """
    Number_of_subscribers: This function queries the Reddit API
    Args:
        subreddit (str): The api subreddit to send a get request to.
    Return: The number of subscribers (not active users, total subscribers)
            for a given subreddit. If an invalid subreddit is given,
            the function should return 0.
    """
    import requests
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'MyServer/1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    try:
        result = response.json()['data']['children'][1]['data']
        return result.get('subreddit_subscribers')
    except IndexError:
        return 0
