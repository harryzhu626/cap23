from collections import defaultdict
import matplotlib.pyplot as plt
from helper.datehelper import sort_and_pad_dates

positive_counts = defaultdict(int)
negative_counts = defaultdict(int)


def congregate_data(opinions):
    for opinion, date in opinions:
        if opinion == 'POSITIVE':
            positive_counts[date] += 1
        elif opinion == 'NEGATIVE':
            negative_counts[date] -= 1
        yield date, opinion


def visualize_for_date(movie_title, opinions):
    dates = list(set([date for date, _ in opinions]))
    dates = sort_and_pad_dates(dates)
    print('sorted ', dates)

    positive_values = [positive_counts[date] for date in dates]
    negative_values = [negative_counts[date] for date in dates]

    plt.clf()

    plt.bar(dates, positive_values, color='blue', label='positive', width=0.3)
    plt.bar(dates, negative_values, color='red', label='negative', width=0.3)

    plt.xlabel('date')
    plt.ylabel('number of opinions')
    plt.title(f'{movie_title} opinion over time')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    return plt