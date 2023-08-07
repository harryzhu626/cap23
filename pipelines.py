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
    opinion_mine_subs(retrieved_subs)
    

from db.sqlite_new import sql_query_k
import pprint 

def pipeline3(
        table_name: str,
        columns: str, 
        query_size: int, 
    ):
    """ Visualization 
    
    """
    sql_output = sql_query_k(columns, table_name, query_size)
    for item in sql_output:
        pprint.pprint(item)