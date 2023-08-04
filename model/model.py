from transformers import pipeline 
# # from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sa_pipe = pipeline('text-classification')