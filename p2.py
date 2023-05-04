from db.mongodb import mongo_query_k
# from model.model import opinion_mine_multi
import pprint 

def pipeline2(k):
    retrieved = mongo_query_k(k)
    for item in retrieved:
        pprint.pprint(item)