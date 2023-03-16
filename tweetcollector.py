import snscrape.modules.twitter as sntwt
import json 
import itertools
import datetime 
import os


current_date = datetime.date.today()
current_date_dir = f"{current_date}"
parent_dir = os.getcwd()
current_date_dir_path = os.path.join(parent_dir, 'data', current_date_dir)
if not os.path.exists(current_date_dir_path):
    os.makedirs(current_date_dir_path)
print(f'directory path {current_date_dir_path}')


def collect_domains(origin, domain_list, dates, top_k=1):
    print('FLAG collect_domains')
    generator_list = []

    for string in domain_list:
        sns_output = snscrape(origin, string, dates)
        tweet_generator = return_generator(sns_output)
        tweet_gen_topk = slice_generator(tweet_generator, top_k)
        generator_list.append(tweet_gen_topk)
    return generator_list
            

def write_db(origin, domain_list, dates, top_k=1):
    for entity in domain_list:
        sns_output = snscrape(origin, entity, dates)
        tweet_generator = return_generator(sns_output)
        tweet_gen_topk = slice_generator(tweet_generator, top_k)

        json_filename = f'data/{current_date}/{entity}({dates[0]}:{dates[1]}).json'
        # print('storage json filename: \n', json_filename)

        with open(json_filename, 'w') as output_file:
            for tweet in tweet_gen_topk:
                json_obj = json.loads(tweet)
                json.dump(json_obj, output_file)
                output_file.write('\n')


def slice_generator(generator, top_k):
    return itertools.islice(generator, top_k)

def snscrape(origin: str, string: str, dates):
    print('FLAG snscrape')
    query_text = f'{string} since:{dates[0]} until:{dates[1]} lang:en'
    print(f'query text {query_text}')
    return sntwt.TwitterHashtagScraper(query_text)


# because multiple hashtags are not guaranteed to be in hashtag form, this function filters out tweets by looking into its hashtags
# to be implemented later
# maybe it should filter out other character/product hashtags as well to keep it clean ...
def hashtag_filter():
    raise NotImplementedError


# convert snscrape query result into a generator
def return_generator(query):
    for tweet in query.get_items():
        yield tweet.json()
# snscrape guide
# until: starts from the given date and goes backward in time
#   e.g. until:2023-01-10 starts from 1-9 and goes to 1-8, 1-7 and so on. 
# if you enter two or more terms for TwitterHashtagScraper, one term is guaranteed to be in hashtags but the other two 
# might be user title or tweet content 