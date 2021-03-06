#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], aftervalue="aftervalue"):
    """total hot post"""
    header = {"User-Agent": "Bryan"}
    if aftervalue == "aftervalue":
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    else:
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json?after=" \
            + aftervalue
    html = requests.get(url, headers=header, allow_redirects=False)
    if html.status_code != 200:
        return None

    data = html.json().get("data")
    after = html.json().get("data").get("after")
    children = data.get("children")
    for i in children:
        titles = i.get("data").get("title")
        hot_list.append(titles)
    if after:
        return (recurse(subreddit, hot_list, after))
    return(hot_list)


if __name__ == "__main__":
    pass
