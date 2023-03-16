from typing import Union, List, Tuple, Iterable, Dict

from utils import timer
from text_processing import TextProcessing
from customized_text_processing import CustomizedTextProcessing

from mongo_db import insert_db_index, query_db_index

from nltk.tokenize import word_tokenize
from collections import defaultdict

# text_processor = TextProcessing.from_nltk()
# include your customized text processing class
text_processor = CustomizedTextProcessing.from_customized()

@timer
def build_inverted_index(wapo_docs: Iterable) -> None:
    """
    load wapo_pa3.jl to build the inverted index and insert the index by using mongo_db.insert_db_index method
    :param wapo_docs:
    :return:
    """
    # TODO:
    # create a inverted index dict, where normalized tokens are keys and list of doc id are values 
    def default_value():
        return []
    inverted_index = defaultdict(default_value)

    # go thru every doc 
    for doc in wapo_docs:
        # put title+content_str thru text_processor to generate a set of normalized tokens
        tokens = text_processor.get_normalized_tokens(doc['title'], doc['content_str'])
        # add tokens as key and doc id as value to inverted_index 
        for token in tokens:
            inverted_index[token].append(doc['id'])
    
    inverted_index = dict_to_list(inverted_index)
    #print('inverted', inverted_index)
    insert_db_index(inverted_index)


def dict_to_list(inverted_index: Dict) -> List:
    result = []
    for key, value in inverted_index.items():
        result.append({"token": key, "doc_ids": value})
    return result


def intersection(posting_lists: List[List[int]]) -> List[int]:
    """
    implementation of the intersection of a list of posting lists that have been ordered from the shortest to the longest
    :param posting_lists:
    :return:
    """
    # TODO:
    if posting_lists:
        inter = set(posting_lists[0])
        for i in range(1, len(posting_lists)):
            inter = inter.intersection(set(posting_lists[i]))
        return list(inter)
    else:
        return []


def query_inverted_index(query: str) -> Tuple[List[int], List[str], List[str]]:
    """
    conjunctive query over the built index by using mongo_db.query_db_index method
    return a list of matched document ids, a list of stop words and a list of unknown words separately
    :param query: user input query
    :return:
    """
    # TODO:
    query_tokens = text_processor.get_normalized_tokens(query, '')

    postings = []
    unknown_list = []
    stopword_list = find_query_stopwords(query)

    for token in query_tokens:
        if token:
            posting = query_db_index(token)
            if posting:
                postings.append(posting)
            else:
                unknown_list.append(token)

    doc_ids = intersection(postings)
    return doc_ids, stopword_list, unknown_list

def find_query_stopwords(query):
    tokens = word_tokenize(query)
    return [token for token in tokens if token in text_processor.STOP_WORDS]