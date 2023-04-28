from transformers import pipeline 

pipe = pipeline('text-classification')

def opinion_mine(sentence):
    return pipe(sentence)