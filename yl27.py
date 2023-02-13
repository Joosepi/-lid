import praw

# Loome ühenduse Redditi rakenduse programmeerimisrajatisega (PRAW) kasutades oma autentimisandmeid
reddit = praw.Reddit(
    client_id="12345",  # Rakenduse ID
    client_secret="ooga booga",  # Rakenduse saladus
    user_agent="Joosep",  # Kasutaja agent nimi
)

# Kontrollime, kas meie ühendus on read-only režiimis
print(reddit.read_only)

# Leian ja trükin välja 10 populaarseimat postitust subredditis "eesti"
for submission in reddit.subreddit("eesti").hot(limit=10):
    print(submission.title)
