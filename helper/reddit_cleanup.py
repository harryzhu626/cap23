def comment_cleanup(comments):

    comment_list = []
    for comment in comments:
        comment_clean = {
            'body': comment.body, 
            'score': comment.score, 
            'permalink': comment.permalink, 
            'author': comment.author.name
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
        'retrieved': False, 
        'title': submission.title, 
        'text': submission.selftext, 
        'score': submission.score, 
        'upvote_ratio': submission.upvote_ratio, 
        'num_comments': submission.num_comments, 
        'permalink': 'reddit.com'+submission.permalink, 
        'author': {'name': submission.author.name, 'karma': 0}, 
        'comments': comment_cleanup(submission.comments.list()), 
        #'top_comments': comment_cleanup(list(submission.comments))
    }
    
    return submission_clean 