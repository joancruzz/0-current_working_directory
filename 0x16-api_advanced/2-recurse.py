#!/usr/bin/python3                                                                                                         
# queries the Reddit API and returns a list containing
# the titles of all hot articles for a given subreddit
from requests import get
url = 'https://www.reddit.com'
headers = {'User-Agent': 'alaksatti'}


def recurse(subreddit, hot_list=[], next_page=None):
    '''recursive function to return list of hot articles'''
    subreddit_page = url + '/r/' + subreddit + '/hot.json'
    if next_page:
        subreddit_page = subreddit_page + '?after=' + next_page

    r = get(subreddit_page, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    list_elements = r.json().get('data').get('children')
    next_page = r.json().get('data').get('after')

    for e in list_elements:
        hot_list.append(e.get('data').get('title'))
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    return hot_list
