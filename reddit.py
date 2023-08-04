from helper.reddit_cleanup import submission_cleanup
import operator 

import pprint

pp = pprint.PrettyPrinter(indent=2)


flair = 'Official Discussion'
filter_text = 'Megathread'

def get_comments(submission):
    top_level_comments = list(submission.comments)
    # all_comments = submission.comments.list()
    print(f'top level comments: {top_level_comments}')


def subreddit_flaired_retrieve_k(subreddit, flair, collect_num):
    submissions_flaired = subreddit.search(
        query=f'flair_text: "{flair}"',
        #query=f'NOT title: Official Discussion ',
        sort='new', 
        limit=collect_num
    )
    for sub in submissions_flaired:
        sub_clean = submission_cleanup(sub)
        yield sub_clean


def reddit_retrieve_k(subreddit, order_type, k):
    # subreddit has submission instances: controversial, gilded, hot, new, rising, top 
    type_getter = operator.attrgetter(order_type)
    submission_getter = type_getter(subreddit)

    for submission in submission_getter(limit=k):
        counter += 1
        if submission.link_flair_text == flair and filter_text not in submission.title:
            submission_clean = submission_cleanup(submission)
            yield submission_clean