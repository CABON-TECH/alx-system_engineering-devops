#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not).

Requirements:
- Prototype: def count_words(subreddit, word_list)
- Note: You may change the prototype, but it must be able to be called with
  just a subreddit supplied and a list of keywords. AKA you can add a counter
  or anything else, but the function must work without supplying a starting
  value in the main.
- If word_list contains the same word (case-insensitive), the final count
  should be the sum of each duplicate (example below with java)
- Results should be printed in descending order, by the count, and if the
  count is the same for separate keywords, they should then be sorted
  alphabetically (ascending, from A to Z). Words with no matches should be
  skipped and not printed. Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it
  appears in. java java java counts as 3 separate occurrences of java.
- To make life easier, java. or java! or java_ should not count as java
- If no posts match or the subreddit is invalid, print nothing.

NOTE: Invalid subreddits may return a redirect to search results. Ensure that
      you are NOT following redirects.
Your code will NOT pass if you are using a loop and not recursively calling
the function! This can be done with a loop but the point is to use a
recursive function. :)
"""
import requests
after = None


def count_words(subreddit, word_list):
    """ I will insert this doc later """
    my_list = recurse(subreddit)
    my_dict = {}

    if my_list:
        for word in word_list:
            my_dict[word] = 0

        for title in my_list:
            title_split = title.split(" ")

            for iter in title_split:
                for iter_split in word_list:
                    if iter.lower() == iter_split.lower():
                        my_dict[iter_split] += 1

        for key, val in sorted(my_dict.items(),  key=lambda x: x[1],
                               reverse=True):
            if val != 0:
                print("{}: {}".format(key, val))


def recurse(subreddit, hot_list=[]):
    """ I will also insert this doc later """
    global after
    headers = {'User-Agent': 'ledbag123'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
    if response.status_code == 200:
        prox = response.json().get('data').get('after')

        if prox is not None:
            after = prox
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')

        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return None
