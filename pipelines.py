from db.mongodb import mongo_multi_insert, mongo_remove
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
    mongo_remove()


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
    

from db.sqlite_new import sql_query_join
from visualize import congregate_data, visualize_for_date

def pipeline3(
        movie_name: str, 
    ):
    """ Visualization 
    
    """
    sql_output = sql_query_join(movie_name=movie_name)
    opinions = congregate_data(sql_output)
    visualize_for_date(opinions)