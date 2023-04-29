from p1 import pipeline1
from p2 import pipeline2
# from p3 import pipeline3
import praw 

from keys.reddit_keys import reddit_agent, reddit_id, reddit_secret

# create a read-only reddit instance，i.e. only access public information 
reddit = praw.Reddit(
    client_id=reddit_id,
    client_secret=reddit_secret,
    user_agent=reddit_agent,
)

# obtain a subreddit
stock_sub = reddit.subreddit("StockMarket")
# stock market opinion on reddit vs stock price 

start_year = 2021
end_year = 2022

reddit_directory = '/data/reddit/'

col_name = 'reddit_raw'
sortby = 'new'

if __name__ == "__main__":
    pipeline1(col_name, stock_sub, sortby)
    # pipeline2()