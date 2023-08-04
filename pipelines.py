from db.mongodb import mongo_multi_insert
from reddit import subreddit_flaired_retrieve_k

def pipeline1(
        subreddit: str, flair: str, collect_num: int
    ) -> None:
    """ DATA
    retrieve submissions from specified subreddit using praw, clean them up, store in mongodb

    Arguments:
    subreddit: name of subreddit
    flair: submission flair 
    collect_num: number of submissions to retrieve
    """
    submission_iterator = subreddit_flaired_retrieve_k(subreddit, flair, collect_num)
    mongo_multi_insert(submission_iterator)


from db.mongodb import mongo_query_k
from db.sqlite import sql_multi_insert
from opinionmine import opinion_mine_subs

def pipeline2(
        retrieve_num: int
    ) -> None:
    """ NLP
    retrieved cleaned submission from mongodb, opinion mine, store opinions in sql
    
    Arguments:
    retrieve_num: number of clean submissions to retrieve
    """
    retrieved_subs = mongo_query_k(retrieve_num)
    subs_opinions_infos = opinion_mine_subs(retrieved_subs)
    sql_multi_insert(subs_opinions_infos)

from db.sqlite import sql_query_k
import pprint 

def pipeline3(
        submission: str,
    ):
    """ 
    
    """
    sql_output = sql_query_k(k)
    for item in sql_output:
        pprint.pprint(item)


# def pipeline4():
#     """ Visualization 
    
#     """