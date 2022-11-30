#!/usr/bin/python3
"""
    This module provides a function that sends a get request to the Reddit API
    with the specified subreddit then process the response and prints the
    titles of the first 10 hot posts listed for a given subreddit
"""


def top_ten(subreddit):
    """
    top_ten: This function queries the Reddit API
    Args:
        subreddit (str): The api subreddit to send a get request to.
    Return: None
    """

    import requests

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    headers = {'User-Agent': 'MyServer/1.0'}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('None')
    try:
        children = response.json()['data']['children']
        for child in children:
            print(child['data'].get('title'))
    except IndexError:
        print('None')
