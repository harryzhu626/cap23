from model.model import sa_pipe
from typing import Dict, List, Tuple
from db.sqlite_new import sql_insert
import sqlite3
from nltk.tokenize import sent_tokenize 
from helper.tokenizer import split_into_sentences

def sentiment_analyze(
        text: str
    ) -> str:
    """perform sentiment analysis on text 
    
    Arguments:
    text: the content of a comment-sentence 
    """
    return sa_pipe(text)


def comment_to_sentences(comment: str):
    """Break a comment string into individual sentences. 
    
    TODO: get rid of empty strings
    Arguments:
    comment: the comment string
    """
    # comment_sentences = comment['body'].lower().split('.')
    # comment_sentences = '\n'.join(comment_sentences).split('\n')
    # return comment_sentences
    return sent_tokenize(comment)

def submission_to_opinion(
        submission_clean: Dict[str, str]
    ):
    """ turn submission_clean JSON into opinions
    
    Arguments:
    submission_clean: ...
    """
    comments = submission_clean['document']['comments']
    sub_opinions_infos = []
    sub = submission_clean['document']

    for comment in comments:

        comment_sentences = comment_to_sentences(comment)

        comment_sentences_opinions = [(sentence, sentiment_analyze(sentence)[0]['label']) for sentence in comment_sentences if sentence]
        
        for sentence_opinion in comment_sentences_opinions:
            appendage = (
                sentence_opinion[0], sentence_opinion[1],
                comment['body'], comment['score'], comment['date'], 'reddit.com'+comment['permalink'],
                sub['title'], sub['score'], # sub['upvote_ratio'], sub['num_comments']
            )
            
            # sub_opinions_infos.append(appendage)
            yield appendage

def sub_to_opinion_to_sql(
        submission_clean: Dict[str, str]
    ):
    """ opinion mine on comments and insert to sqlite db 
    """
    # comments = submission_clean['document']['comments']
    # sub_opinions_infos = []
    sub = submission_clean['document']
    comments = sub['comments']

    movie_info = ([sub['title'], sub['score'], sub['permalink']])
    comment_infos = []

    for comment in comments:
        comment_sentences = split_into_sentences(comment['body'])

        sentence_holder = [(sentence, sentiment_analyze(sentence)[0]['label'], 'none') for sentence in comment_sentences]
        comment_infos.append(([comment['body'], comment['score'], comment['date'], 'reddit.com'+comment['permalink']], sentence_holder))

    sql_insert(movie_info, comment_infos)


def opinion_mine_subs(
        submissions_clean
    ) -> None:
    for submission in submissions_clean:
        sub_to_opinion_to_sql(submission)