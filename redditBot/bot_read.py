#!/usr/bin/python3
import praw

reddit = praw.Reddit('scottgrimesbot')

subreddit = reddit.subreddit("scottgrimesfanclub")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
