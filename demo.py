#!/usr/bin/python3

# From the PRAW quickstart guide.

import praw

from oauth import oauth

user_agent="Python3:rustplaybot:v0.0.0 (by /u/rustplaybot)"

reddit = praw.Reddit(
    client_id=oauth["client_id"],
    client_secret=oauth["client_secret"],
    user_agent=user_agent,
)
submissions = reddit.subreddit("rust").hot(limit=5)
for s in submissions:
    print(s.title)
