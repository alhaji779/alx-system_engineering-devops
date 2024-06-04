#!/usr/bin/python3

import sys
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Returns a list of titles of all hot articles
       for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla 5.0.0"}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except Exception:
        return None


if __name__ == "__main__":
    recurse(argv[1])
