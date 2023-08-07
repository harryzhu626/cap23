from pipelines import pipeline1, pipeline2, pipeline3
import praw 
from keys.reddit_keys import reddit_agent, reddit_id, reddit_secret

# create a read-only reddit instance，i.e. only access public information 
reddit = praw.Reddit(
    client_id=reddit_id,
    client_secret=reddit_secret,
    user_agent=reddit_agent,
)

# obtain a subreddit
subreddit = reddit.subreddit("movies")
flair_text = 'Official Discussion'
# stock market opinion on reddit vs stock price 

reddit_directory = '/data/reddit/'
collect_num = 2
retrieve_num = 2
sortby = 'hot' # submission types: controversial, gilded, hot, new, rising, top 

table_name = 'sentences'
columns = 'comment_id, content, opinion, aspect'
query_size = 5

if __name__ == "__main__":
    # pipeline1(subreddit, flair_text, collect_num)
    # pipeline2(retrieve_num)
    pipeline3(columns=columns, table_name=table_name, query_size=query_size)