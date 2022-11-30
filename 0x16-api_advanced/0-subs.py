#!/usr/bin/python3

"""
    This script takes input from the command line
    then process data from the Reddit API with the specified endpoint.
"""


def number_of_subscribers(endpoint):
    """
    Number_of_subscribers: This function queries the Reddit API
    Args:
        endpoint (str): The api endpoint to send a get request to.
    Return: The number of subscribers (not active users, total subscribers)
            for a given subreddit. If an invalid subreddit is given,
            the function should return 0.
    """
    import requests
    url = f'https://www.reddit.com/r/{endpoint}.json'
    headers = {'User-Agent': 'MyServer/1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    try:
        result = response.json()['data']['children'][1]['data']
        return result.get('subreddit_subscribers')
    except IndexError:
        return 0
