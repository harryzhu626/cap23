"""
directory: cap23
module: tweettodb.py
author: harry z
description: 
this module is 1 of the 3 pipeline modules. it handles extracting tweets and storing them in non-relational db;
imported by: this module should be imported by pipelines.py;
import: this module should import from tweetcollector.py, mongo.py
"""

from tweetcollector import collect_domains, write_db
from mongo import insert_tweets
from dategenerator import create_dates
import itertools 

origin_handle = 'genshinimpact'
domain_list = [
    'diluc',
    'jean',
    'xinyan', 
]
output_generator = True

date_start_year = 2022
date_start_month = 1
date_end_year = 2022
date_end_month = 2

top_k = 10

# date_example = 'until:2023-01-10', 'since:2021-01-01'
dates = create_dates(date_start_year, date_end_year, 
                     date_start_month, date_end_month)


def tweettodb_main():
    if output_generator:
        tweet_generators = collect_domains(origin_handle, domain_list, dates, top_k=top_k)
        for generator in tweet_generators: # one generator for each entity in domain_list 
            print(f'FLAG insert gen to db')
            insert_tweets(generator)
    else:
        print(f'FLAG writing tweets to db')
        write_db(origin_handle, domain_list, dates, top_k) 