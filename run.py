from input import user_input
from domain_extractor import extract_domain
from tweetcollector import collect_tweet
from visualizer import visualize 
from sentimentanalysis import analyze_sentiment

# runs the application 
# --train for training model, --run for inference
def run():
    # user input
    origin_handle, domain, performance = user_input()

    # if no domain is given, use origin_handle to extract domain
    if not domain:
        domain = extract_domain(origin_handle)
    
    # use origin and domain to collect tweets, and load into database 
    collect_tweet(origin_handle, domain)

    # perform sentiment analysis on database tweets 
    sentiment = analyze_sentiment()

    # visualize sentiments against performance 
    visualize(sentiment, performance)