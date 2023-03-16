"""
directory: cap23
module: mongo.py
author: harry z
description: 
this module 
"""

import pymongo 
from typing import Iterable

# connect to mongodb server running on local host
client = pymongo.MongoClient(
    'localhost', 27017
)
db = client['cap_db']


def insert_tweets(tweets: Iterable) -> None:
    """
    create a collection called 'tweets_col'
    add a unique ascending index on the key 'tweet_id'
    insert tweet jsons into the 'tweets_col' collection
    :param tweets: tweet json iterator
    :return: 
    """

    db_tweets = db['tweets_col']
    for i, tweet in enumerate(tweets):
        # add other key/value like 'user', 'date'
        db_tweets.insert_one({'tweet_id': i, 'json': tweet}) 


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