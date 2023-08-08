import praw
import pprint
from datetime import datetime

def comment_cleanup(comments):

    comment_list = []
    for comment in comments:
        
        # only append top level comments, ignore MoreComments trees
        if isinstance(comment, praw.models.reddit.comment.Comment):
            date_d = datetime.fromtimestamp(comment.created_utc).strftime("%A, %B %d, %Y %H:%M:%S")
            comment_clean = {
                'body': comment.body,
                'score': comment.score,
                'date': date_d,
                'permalink': comment.permalink,
                # deleted users will be Nonetype 
                # 'author': None if comment.author == None else comment.author.name,
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
        # 'text': submission.selftext, 
        # 'flair': submission.link_flair_text, 
        'score': submission.score, 
        'upvote_ratio': submission.upvote_ratio, 
        'num_comments': submission.num_comments, 
        'permalink': 'reddit.com'+submission.permalink, 
        #'author': None if submission.author == None else submission.author.name, 
        'comments': comment_cleanup(submission.comments.list()), 
        # comment_timestamp add
    }
    
    return submission_clean 