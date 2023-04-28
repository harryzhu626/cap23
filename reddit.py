import praw 
import pprint
from keys.reddit_keys import reddit_agent, reddit_id, reddit_secret

# create a read-only reddit instance，i.e. only access public information 
reddit = praw.Reddit(
    client_id=reddit_id,
    client_secret=reddit_secret,
    user_agent=reddit_agent,
)

# obtain a subreddit
gi_sub = reddit.subreddit("Genshin_Impact")

stock_sub = reddit.subreddit("StockMarket")
# stock market opinion on reddit vs stock price 

start_year = 2021
end_year = 2022

reddit_data = '/data/reddit/'

def get_comments(submission):
    top_level_comments = list(submission.comments)
    # all_comments = submission.comments.list()
    print(f'top level comments: {top_level_comments}')

def reddit_retrieve_k(subreddit, order_type, k):
    # subreddit has submission instances: controversial, gilded, hot, new, rising, top 
    for submission in stock_sub.new(limit=k):
        #print('post title', submission.title)
        #print('post author', submission.author.name)
        # get_comments(submission)
        # pprint.pprint(vars(submission))
        output = (submission.title, submission.author.name)
        pprint.pprint(vars(submission))
        yield output