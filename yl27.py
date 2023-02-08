import praw

reddit = praw.Reddit(
    client_id="12345",
    client_secret="ooga booga",
    user_agent="Joosep",
)

print(reddit.read_only)

for submission in reddit.subreddit("eesti").hot(limit=10):
    print(submission.title)