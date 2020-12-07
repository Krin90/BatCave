import praw
import re


reddit = praw.Reddit('JoshAllen')


subreddit = reddit.subreddit('denverbroncos')


for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Josh Allen", comment.body, re.IGNORECASE):
        reply = "Not drafting Josh Allen is the biggest mistake of the last 5 years"
        comment.reply(reply)
        print(reply)
