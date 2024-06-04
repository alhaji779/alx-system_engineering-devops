#!/usr/bin/python3

import sys
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles
       for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
