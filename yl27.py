import praw

reddit = praw.Reddit(
    client_id="OoQ-Lkq0te53DvFLHtqQeQ",
    client_secret="IV890cYzv0cWeMZ4cJn2_XxKyd66TA",
    user_agent="python:OoQ-Lkq0te53DvFLHtqQeQ:v0.1 (by u/TAK-22 testing)",
)

print(reddit.read_only)

for submission in reddit.subreddit("eesti").hot(limit=10):
    print(submission.title)