from mongo import query_tweet, query_k
from transformers import pipeline 


pipe = pipeline('text-classification')
query_size = 1


def retrieve_tweets():
    return query_k(query_size)


def analyze_sentiment(sentence):
    return pipe(sentence)