"""
directory: cap23
module: mongodb.py
author: harry z
"""

import pymongo 
from typing import Iterable

# connect to mongodb server running on local host
client = pymongo.MongoClient(
    'localhost', 27017
)
db = client['cap_db']

db_reddit_raw = db['reddit_raw']
db_reddit_clean = db['reddit_clean']

raw_id = 0      # keeps track of number of raw documents stored in db_reddit_raw
clean_id = 0    # keeps track of number of clean documents stored in db_reddit_clean 

raw_id_retrieved = 0    # keeps track of number of raw documents retrieved from db_reddit_raw
clean_id_retrieved = 0  # keeps track of number of clean documents retrieved from db_reddit_clean 

def mongo_single_insert(db_col, doc_id, document) -> None:
    """
    depends on db_col and doc_id, insert into db_reddit_raw or db_reddit_clean 
    """
    db_col.insert_one({'doc_id': doc_id, 'document': document})


def mongo_multi_insert(col_name, documents: Iterable) -> None:
    """
    :param col_name: collection name; documents: iterable for documents
    :return: none 
    """

    db_col = db_reddit_raw
    doc_id = raw_id
    if col_name == 'reddit_clean':
        db_col = db_reddit_clean
        doc_id = clean_id
    
    for document in documents:
        mongo_single_insert(db_col, doc_id, document)


def query_tweet(tweet_id: int) -> None:
    """
    given a tweet id, retrieve the tweet json 
    :param tweet_id:
    :return:
    """
    cursor = db['tweets_col'].find({'tweet_id': tweet_id})

    cursor_temp = cursor.clone()
    if len(list(cursor_temp)) > 0:
        return cursor
    return 


def mongo_query_k(col_name, query_size_k):
    starting_id = raw_id 
    db_col = db_reddit_raw
    if col_name == 'reddit_clean':
        starting_id = clean_id 
        db_col = db_reddit_clean 
    end_id = starting_id + query_size_k 

    return db_col.find().limit(query_size_k)