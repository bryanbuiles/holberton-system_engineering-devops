#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """total subs"""
    header = {"User-Agent": "Bryan"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    html = requests.get(url, headers=header, allow_redirects=False)
    if html.status_code == 200:
        data = html.json().get("data")
        return data.get("subscribers")
    else:
        return 0


if __name__ == "__main__":
    pass
