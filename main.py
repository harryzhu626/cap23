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
collect_num = 30
opinionmine_num = 4
sortby = 'hot' # submission types: controversial, gilded, hot, new, rising, top 

movie_name = 'official discussion - haunted mansion [spoilers]'
table_name = 'sentences'
columns = 'comment_id, content, opinion, aspect'
query_size = 5

if __name__ == "__main__":
    # pipeline1(subreddit, flair_text, collect_num)
    #pipeline2(opinionmine_num)
    pipeline3(movie_name=movie_name)