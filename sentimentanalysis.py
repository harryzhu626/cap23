from mongo import query_tweet, query_k

query_size = 3
def retrieve_tweets():
    return query_k(query_size)


def analyze_sentiment():
    # return sentiments 
    raise NotImplementedError