#!/usr/bin/python3
# Function that queries the Reddit API and prints the titles
# of the first 10 hot posts listed for a given subreddit.

from requests import get


def top_ten(subreddit):
    '''first 10 hot posts listed for a given subreddit'''
    r = get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
            headers={"User-agent": "joancruz"}, allow_redirects=False)
    if r.status_code != 200:
        print(None)
    else:
        for key in r.json().get('data').get('children'):
            print(key.get('data').get('title'))
