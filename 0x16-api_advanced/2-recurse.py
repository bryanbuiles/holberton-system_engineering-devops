import requests


def recurse(subreddit, hot_list=[], aftervalue="aftervalue"):
    """total subs"""
    header = {"User-Agent": "Bryan"}
    if aftervalue == "aftervalue":
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    else:
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json?after=" \
            + aftervalue
    html = requests.get(url, headers=header, allow_redirects=False)
    if html.status_code == 200:
        after = html.json().get("data").get("after")
        for i in html.json().get("data", None).get("children", None):
            hot_list.append(i.get("data", None).get("title", None))
        if after:
            return (recurse(subreddit, hot_list, after))
        return(hot_list)
    else:
        return (None)


if __name__ == "__main__":
    pass
