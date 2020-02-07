#!/usr/bin/python3
# Function that queries the Reddit API
# and returns the number of subscribers

from requests import get
import json
import sys


def number_of_subscribers(subreddit):
    r = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={"User-agent": "joancruz"}, allow_redirects=False)
    if r.status_code is not 200:
        return 0
    else:
        return r.json().get('data').get('subscribers')
