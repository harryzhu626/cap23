from pipelines import pipeline1, pipeline2
import praw 
from keys import user_agent, client_id, client_secret

# Create a read-only reddit instance，i.e. only access public information 
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)

# Obtain the r/movies subreddit. 
subreddit = reddit.subreddit("movies")
# Only submissions with this flair contains official movies discussions
flair_text = 'Official Discussion'

collect_num = 2 # how many submission to collect from reddit 
opinionmine_num = 1 # how many stored submission to opinion mine

if __name__ == "__main__":
    pipeline1(subreddit, flair_text, collect_num)
    pipeline2(opinionmine_num)