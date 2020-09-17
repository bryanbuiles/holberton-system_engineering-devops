#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """total subs"""
    header = {"User-Agent": "Bryan"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json?limit=10"
    html = requests.get(url, headers=header, allow_redirects=False)
    if html.status_code == 200:
        data = html.json().get("data")
        children = data.get("children")
        for i in children:
            titles = i.get("data").get("title")
            print(titles)
    else:
        print(None)


if __name__ == "__main__":
    pass
