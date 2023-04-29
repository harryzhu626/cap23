from database.mongodb import mongo_multi_insert
from reddit import reddit_retrieve_k


def pipeline1(col_name, subreddit, sortby):
    reddit_iterator = reddit_retrieve_k(subreddit, sortby, 2)
    mongo_multi_insert(col_name, reddit_iterator)
    print('inserting')
    
    return 

pipeline1()