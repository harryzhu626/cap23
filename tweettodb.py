from tweetcollector import collect_tweet
from mongo import insert_tweets
from dategenerator import create_dates

origin_handle = 'genshinimpact'
domain_list = [
    'diluc', 
    'jean',
    'dehya', 
]

date_start_year = 2022
date_start_month = 1
date_end_year = 2022
date_end_month = 12

dates = create_dates(date_start_year, date_end_year, 
                     date_start_month, date_end_month)

date_example = 'until:2023-01-10'

print(dates)

# if __name__ == '__main__':
#     collect_tweet(origin_handle, domain_list, dates, todb=False)
#     insert_tweets()