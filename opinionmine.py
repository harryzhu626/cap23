from model.model import sa_pipe
from typing import Dict
from db.sqlite import sql_insert
from helper.tokenizer import split_into_sentences

def sentiment_analyze(
        text: str
    ) -> str:
    """perform sentiment analysis on text 
    
    Arguments:
    text: the content of a comment-sentence 
    """
    return sa_pipe(text)


def sub_to_opinion_to_sql(
        submission_clean: Dict[str, str]
    ):
    """ opinion mine on comments and insert to sqlite db 
    """
    sub = submission_clean['document']
    comments = sub['comments']

    movie_title = sub['title'].split('-')[1].strip()
    if ' [spoilers]' in movie_title:
        movie_title = movie_title[:-11]
    movie_info = ([movie_title, sub['score'], sub['permalink']])
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