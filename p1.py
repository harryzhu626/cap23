from db.mongodb import mongo_multi_insert
from reddit import reddit_retrieve_k

def pipeline1(subreddit, sortby, k):
    reddit_iterator = reddit_retrieve_k(subreddit, sortby, k)
    mongo_multi_insert(reddit_iterator)