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


def insert_opinions(opinions: Iterable) -> None:
    """
    create a collection called 'opinions_col'
    add a unique ascending index on the key 'opinion_id'
    insert opinion jsons into the 'opinions_col' collection
    :param tweets: opinion json iterator
    :return: 
    """
    db_opinions = db['opinions_col']
    for i, opinion in enumerate(opinions):
        db_opinions.insert_one({'opinion_id': i, 'json': opinion})


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


def query_k(query_size):
    # cursor = db['tweets_col'].find().limit(query_size)
    # print('type cursor', type(cursor))
    # clone = cursor.clone()
    # print('len cursor', len(list(cursor)))
    # clone = clone.limit(query_size)
    return db['tweets_col'].find().limit(query_size)