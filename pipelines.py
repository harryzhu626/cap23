# from tweettodb import 
# from dbtosatodb import
# from dbtov import 

# controls the 3 pipelines 
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