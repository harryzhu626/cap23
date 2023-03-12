import snscrape.modules.twitter as sntwt
import json 


def collect_tweet(origin, domain):
    
    query_text = f'{origin} until:2021-01-10 lang:en'

    query = sntwt.TwitterHashtagScraper(query_text)
    count = 0

    with open('tweet011021.json', 'w') as f:

        for tweet in query.get_items():
            #print(count, type(tweet))
            print(f'{vars(tweet)}\n')
            #count += 1
            tweet = tweet.json()
            json_obj = json.loads(tweet)
            # print(tweet)
            json.dump(json_obj, f)
            f.write('\n')



# snscrape guide
# until: starts from the given date and goes backward in time
#   e.g. until:2023-01-10 starts from 1-9 and goes to 1-8. 