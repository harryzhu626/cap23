from typing import Dict, List, Iterable

import pymongo

client = pymongo.MongoClient(
    "localhost", 27017
)  # connect to the mongodb server running on your localhost
db = client["ir_2022_wapo"]  # create a new database called "ir_2022_wapo"


def insert_docs(docs: Iterable) -> None:
    """
    - create a collection called "wapo_docs"
    - add a unique ascending index on the key "id"
    - insert documents into the "wapo_docs" collection
    :param docs: WAPO docs iterator (utils.load_wapo(...))
    :return:
    """
    # TODO:
    db_docs = db['wapo_docs']
    for i, doc in enumerate(docs):
        db_docs.insert_one(doc, {'id': i})


def insert_db_index(index_list: List[Dict]) -> None:
    """
    - create a collection called "inverted_index"
    - add a unique ascending index on the key "token"
    - insert posting lists (index_list) into the "inverted_index" collection
    :param index_list: posting lists in the format of [{"token": "post", "doc_ids": [0, 3, 113, 444, ...]}, {...}, ...]
    :return:
    """
    # TODO:
    db_index = db['inverted_index']
    for i, index in enumerate(index_list):
        db_index.insert_one(index, {'token': i})
    

def query_doc(doc_id: int) -> Dict:
    """
    query the document from "wapo_docs" collection based on the doc_id
    :param doc_id:
    :return:
    """
    # TODO:
    cursor = db['wapo_docs'].find({'id': doc_id})
    return cursor[0]


def query_db_index(token: str) -> Dict:
    """
    query the posting list from "inverted_index" collection based on the token
    :param token:
    :return:
    """
    # TODO:
    cursor = db['inverted_index'].find({'token': token}) 

    cursor_temp = cursor.clone()
    if len(list(cursor_temp)) > 0:
        return cursor[0]['doc_ids']
    else:
        return