from input import user_input
from domain_extractor import extract_domain
from tweetcollector import collect_tweet
from visualizer import visualize 
from sentimentanalysis import analyze_sentiment

# runs the application 
# --train for training model, --run for inference

# the pipeline has 3 concurrent parts: 
#   1 scrape, insert to db 'tweets'
#   2 pull from db 'tweets', perform sentiment analysis, insert to db 'sentiments' 
#   3 pull from db 'sentiments', visualize
# it's scalable, non-linear

# two database: 
#   'tweets': non-relational json database (mongodb) to store scapred tweets.
#   'sentiments': relational database (sqlite) to store processed sentiments. 

# streamlit can handle visualization 