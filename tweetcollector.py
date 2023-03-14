import snscrape.modules.twitter as sntwt
import json 

def new_function(origin, domain_list, dates, todb=False):
    print('wtf')
    for item in domain_list:
        query_text = f'{origin} {item} since:{dates[0]} until:{dates[1]} lang:en'

        print('query text: ', query_text)
        query = sntwt.TwitterHashtagScraper(query_text)
        count = 0

        if todb:
            # if to database, output a generator
            for tweet in query.get_items():
                yield tweet.json()
        else:
            json_filename = f'tweet{origin}{item}{dates[0]}{dates[1]}.json'
            print('json filename: ', json_filename)

            with open(json_filename, 'w') as f:
                for tweet in query.get_items():
                    print(count, type(tweet))
                    print(f'{vars(tweet)}\n')
                    count += 1
                    tweet = tweet.json()
                    json_obj = json.loads(tweet)
                    json.dump(json_obj, f)
                    f.write('\n')

def collect_tweet(origin, domain_list, dates, todb=False):
    text = input('type smth')
    for item in domain_list:
        query_text = f'{origin} {item} since:{dates[0]} until:{dates[1]} lang:en'

        print('query text: ', query_text)
        query = sntwt.TwitterHashtagScraper(query_text)
        count = 0

        if todb:
            # if to database, output a generator 
            for tweet in query.get_items():
                yield tweet.json()
        else:
            json_filename = f'tweet{origin}{item}{dates[0]}{dates[1]}.json'
            print('json filename: ', json_filename)

            with open(json_filename, 'w') as f:
                for tweet in query.get_items():
                    print(count, type(tweet))
                    print(f'{vars(tweet)}\n')
                    count += 1
                    tweet = tweet.json()
                    json_obj = json.loads(tweet)
                    json.dump(json_obj, f)
                    f.write('\n')


# snscrape guide
# until: starts from the given date and goes backward in time
#   e.g. until:2023-01-10 starts from 1-9 and goes to 1-8, 1-7 and so on. 