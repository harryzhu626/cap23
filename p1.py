from database.mongodb import mongo_multi_insert, mongo_single_insert, mongo_query_k
from reddit import reddit_retrieve_k

col_name = 'reddit_raw'
subreddit_name = 'stock'

def pipeline1():
    reddit_iterator = reddit_retrieve_k(subreddit_name, 'new', 1)
    mongo_multi_insert(col_name, reddit_iterator)
    print('retrieving')
    retrieved = mongo_query_k(col_name, 2)
    for item in retrieved:
        print(item)

print("insering")
pipeline1()
print("ending")