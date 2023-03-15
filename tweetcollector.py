import snscrape.modules.twitter as sntwt
import json 

def new_function(origin, domain_list, dates, todb=False):
    generator_list = []

    item = domain_list[0]
    query_text = 'genshinimpact'

    query = sntwt.TwitterHashtagScraper(query_text)
    print('query', type(query))
    for tweet in query.get_items():
        print('tweet', type(tweet))
        print(f'{vars(tweet)}')


def collect_tweet(origin, domain_list, dates, todb=False):
    print('flag collect_tweet')
    for item in domain_list:
        query_text = f'{item} max-results:2 since:{dates[0]} until:{dates[1]} lang:en'

        print('query text: ', query_text)
        query = sntwt.TwitterHashtagScraper(query_text)

        return return_generator(query)

        # if todb:
        #     # if to database, output a generator 
        #     for tweet in query.get_items():
        #         yield tweet.json()
        # if todb:
        #     json_filename = f'data/{item}{dates[0]}{dates[1]}.json'
        #     print('json filename: ', json_filename)

        #     with open(json_filename, 'w') as f:
        #         for tweet in query.get_items():
        #             print(f'{vars(tweet)}\n')
        #             tweet = tweet.json()
        #             json_obj = json.loads(tweet)
        #             json.dump(json_obj, f)
        #             f.write('\n')

def return_generator(query):
    for tweet in query.get_items():
        yield tweet.json()
# snscrape guide
# until: starts from the given date and goes backward in time
#   e.g. until:2023-01-10 starts from 1-9 and goes to 1-8, 1-7 and so on. 