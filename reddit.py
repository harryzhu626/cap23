from helper.reddit_cleanup import submission_cleanup

def get_comments(submission):
    top_level_comments = list(submission.comments)
    # all_comments = submission.comments.list()
    print(f'top level comments: {top_level_comments}')


def reddit_retrieve_k(subreddit, order_type, k):
    # subreddit has submission instances: controversial, gilded, hot, new, rising, top 
    for submission in subreddit.new(limit=k):
        submission_clean = submission_cleanup(submission)
        yield submission_clean