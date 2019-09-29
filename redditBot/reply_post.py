#!/usr/bin/python3
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('scottgrimesbot')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 posts from subreddit  
subreddit = reddit.subreddit('scottgrimesfanclub')
for submission in subreddit.hot(limit=5):
    print("submission title:", submission.title)
    
    # If we haven't replied to the post before
    if submission.id not in posts_replied_to:
    
        # Do a case insensitive search
        if re.search("i love scott grimes", submission.title, re.IGNORECASE):
            # Reply to post
            submission.reply("I also love Scott Grimes!")
            print("Bot replying to:", submission.title)
            
            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")