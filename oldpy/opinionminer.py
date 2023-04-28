from database.mongodb import query_tweet, query_k
from transformers import pipeline 
from typing import Iterable
import json

pipe = pipeline('text-classification')
query_size = 2


def retrieve_tweets():
    return query_k(query_size)


def analyze_opinion(sentence):
    return pipe(sentence)


def analyze_tweets(tweets: Iterable):
    for tweet in tweets:
        content, attributes = extract_content(tweet)
        opinion = analyze_opinion(content)


def extract_content(tweet):
    print(f'FLAG extract content')
    tweet_id = (tweet['tweet_id'], tweet['_id'])
    tweet = json.loads((tweet['json']))
    user = tweet['user']
    
    content_info = {'content':tweet['renderedContent'], 'hashtags': tweet['hashtags'], 'date': tweet['date'], 'url': tweet['url']}
    user_info = {
        'followersCount':user['followersCount'], 'friendsCount': user['friendsCount'], 
        'statusesCount': user['statusesCount'], 'favoritesCount': user['favouritesCount']
    }
    meta_info = {'replyCount': tweet['replyCount'], 'retweetCount': tweet['retweetCount'], 'likeCount': tweet['likeCount'], 'quoteCount': tweet['quoteCount']}
    print(content_info)
    print(user_info)
    print(meta_info)
    return content_info, user_info, meta_info

# 3 major parts of a tweet:
# Tweet content: ‘renderedContent’, ‘hashtags’, ‘retweetedTweet’, ‘quotedTweet’
# Tweet creator: ‘user’: 
# renderedDescription, verified, created, followersCount, friendsCount, statusesCount, favouritesCount, mediaCount
# Tweet meta: ‘replyCount, retweetCount, likeCount, quoteCount
