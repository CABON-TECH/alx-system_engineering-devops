#!/usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Ftn that returns a list containing all hot articles"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
                Safari/537.36 Brave/94.1.23.1 Chrome/94.0.4606.61'
                }

    # parameters for the Reddit API request
    params = {
        "limit": 50,
        "after": after,
        "count": count
    }

    # make the API request
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers, params=params,
        allow_redirects=False
    )

    # validate the response status code
    if response.status_code != 200:
        return None

    # extract the data from the API response
    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    # append the titles of the hot articles to the list
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    # recursively call the function with the next page if there is one
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # return the list of hot article titles
    return hot_list
