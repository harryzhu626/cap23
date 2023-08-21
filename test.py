import praw
import datetime

from keys import user_agent, client_id, client_secret


# create a read-only reddit instance，i.e. only access public information 
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)

# Obtain the r/movies subreddit. 
subreddit = reddit.subreddit("movies")
# We are only interested in submissions this flair
flair_text = 'Official Discussion'

# Define the date range
start_date = datetime.datetime(2023, 7, 20)
end_date = datetime.datetime(2023, 7, 21)

# Search for submissions within the date range
search_results = subreddit.search(
    query='',  # You can specify keywords here if needed
    sort='new',  # Sort by new submissions
    time_filter='day',  # Limit the search to the past month
    after=start_date.timestamp(),
    before=end_date.timestamp()
)

# Loop through the search results
for submission in search_results:
    print(f"Title: {submission.title}")
    print(f"URL: {submission.url}")
    print(f"Created at: {datetime.datetime.fromtimestamp(submission.created_utc)}")
    print("---")
