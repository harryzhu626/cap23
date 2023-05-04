"""
directory: cap23
module: mongodb.py
author: harry z
"""

import pymongo 
from typing import Iterable

# connect to mongodb server running on local host
client = pymongo.MongoClient(
    'localhost', 27017
)
db = client['cap_db']

# db_reddit_raw = db['reddit_raw']
db_reddit_clean = db['reddit_clean']

# raw_id = 0      # keeps track of number of raw documents stored in db_reddit_raw
clean_id = 0    # keeps track of number of clean documents stored in db_reddit_clean 

# raw_id_retrieved = 0    # keeps track of number of raw documents retrieved from db_reddit_raw
clean_id_retrieved = 0  # keeps track of number of clean documents retrieved from db_reddit_clean 

def mongo_single_insert(db_col, doc_id, document) -> None:
    """
    depends on db_col and doc_id, insert into db_reddit_raw or db_reddit_clean 
    """
    db_col.insert_one({'doc_id': doc_id, 'document': document})


def mongo_multi_insert(documents: Iterable) -> None:
    """
    :param col_name: collection name; documents: iterable for documents
    :return: none 
    """
    
    for document in documents:
        mongo_single_insert(db_reddit_clean, clean_id, document)


def mongo_query_k(query_size_k):
    return db_reddit_clean.find().limit(query_size_k)