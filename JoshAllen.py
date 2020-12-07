import praw


reddit = praw.Reddit(client_id='46-O9Fck9EDQkg',
                     client_secret='s66xTLBCc9P6E4KwHbVdy_wJBrDsjg',
                     username='beepbopboopbop117',
                     password='Roland27!',
                     user_agent='JoshAllen by me')


subreddit = reddit.subreddit('DenverBroncos')

keyphrase = 'Josh Allen'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        reply = "Not drafting Josh Allen is the biggest mistake of the last 5 years"
        comment.reply
