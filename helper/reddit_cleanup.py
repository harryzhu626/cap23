import praw
from datehelper import date_trimmer

def comment_cleanup(comments):

    comment_list = []
    for comment in comments:
        
        # only append top level comments, ignore MoreComments trees
        if isinstance(comment, praw.models.reddit.comment.Comment):
            date_d = date_trimmer(comment.created_utc)
            comment_clean = {
                'body': comment.body,
                'score': comment.score,
                'date': date_d,
                'permalink': comment.permalink,
            }
            comment_list.append(comment_clean)
    
    return comment_list

def submission_cleanup(submission):
    """
    keep 
    post:   score, upvote_ratio, awards, permalink, num_comment 
            author: name, karma
            comments: body, score, permalink, author
    """

    submission_clean = {
        # 'retrieved': False, 
        'title': submission.title.lower(), 
        'score': submission.score, 
        'upvote_ratio': submission.upvote_ratio, 
        'num_comments': submission.num_comments, 
        'permalink': 'reddit.com'+submission.permalink, 
        'comments': comment_cleanup(submission.comments.list()), 
        # 'text': submission.selftext, 
        # 'flair': submission.link_flair_text, 
        #'author': None if submission.author == None else submission.author.name, 
    }
    
    return submission_clean 