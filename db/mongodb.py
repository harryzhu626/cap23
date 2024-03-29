"""
directory: cap23
module: mongodb.py
author: harry z
"""

import pymongo 
from typing import Iterable
from variables import mongo_name

# connect to mongodb server running on local host
client = pymongo.MongoClient(
    'localhost', 27017
)
db = client['cap_db']
db_reddit_clean = db[mongo_name]

clean_id = 0    # keeps track of number of documents stored in db_reddit_clean 

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


def mongo_remove():

    # query = {"title": {"$regex": "megathread", "$options": "i"}}  # Case-insensitive search
    last_30_entries = db_reddit_clean.find().sort([("_id", -1)]).limit(30)

    # Delete matching entries from the last 30 entries
    deleted_count = 0
    for entry in last_30_entries:
        if "megathread" in entry['document']["title"]:
            db_reddit_clean.delete_one({"_id": entry["_id"]})
            deleted_count += 1