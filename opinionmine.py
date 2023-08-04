from model.model import sa_pipe
from typing import Dict, List, Tuple

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
    comment_sentences = comment['body'].split('.')
    comment_sentences = '\n'.join(comment_sentences).split('\n')
    return comment_sentences

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

    # return sub_opinions_infos


def opinion_mine_sub(
        submission_clean: Tuple
    ) -> None:
    return submission_to_opinion(submission_clean)

    
def opinion_mine_subs(
        submissions_clean
    ) -> None:
    return [opinion_mine_sub(submission) for submission in submissions_clean]
    # for submission in submissions_clean:
    #     yield opinion_mine_sub(submission)