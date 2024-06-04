#!/usr/bin/python3
""" Function to pull count of subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ function to pull subreddit count
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        datas = response.json()
        ddata = datas['data']['subscribers']
        return ddata
    else:
        return 0
