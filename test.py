import praw
from datetime import datetime, timedelta

from keys.reddit_keys import reddit_agent, reddit_id, reddit_secret

# Replace these values with your own Reddit app credentials
client_id = reddit_id
client_secret = reddit_secret
user_agent = reddit_agent

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def get_top_submissions(subreddit_name, start_date, end_date):
    subreddit = reddit.subreddit(subreddit_name)
    current_date = start_date
    delta = timedelta(days=1)

    while current_date <= end_date:
        print(f'current_date: {current_date}')
        current_unix_timestamp = int(current_date.timestamp())
        next_date = current_date + delta
        next_unix_timestamp = int(next_date.timestamp())

        # Get the top submission for the current day
        top_submission = subreddit.search(
            f'time: {current_unix_timestamp}..{next_unix_timestamp}',
            sort='top',
            time_filter='day',
            limit=1
        )

        print(f'there it is')
        
        # Display the top submission for the current day
        for submission in top_submission:
            print('wtf')
            print(f"Top submission on {current_date.strftime('%Y-%m-%d')}: {submission.title}")

        current_date = next_date

if __name__ == "__main__":
    subreddit_name = 'movies'
    print('here I am')
    # Replace the following with your desired start and end dates
    start_date = datetime(2023, 6, 1)
    end_date = datetime(2023, 6, 4)

    get_top_submissions(subreddit_name, start_date, end_date)
