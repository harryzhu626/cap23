from collections import defaultdict
import matplotlib.pyplot as plt
from helper.datehelper import sort_and_pad_dates

def congregate_data(opinions):
    positive_counts = defaultdict(int)
    negative_counts = defaultdict(int)
    overall = defaultdict(int)
    dates = []

    for opinion, date, _ in opinions:
        dates.append(date)
        if opinion == 'POSITIVE':
            positive_counts[date] += 1
            overall[date] += 1
        elif opinion == 'NEGATIVE':
            negative_counts[date] -= 1
            overall[date] -= 1

    return dates, positive_counts, negative_counts, overall


def calculate_ratios(pos, neg):
    ratios = []
    for value1, value2 in zip(pos, neg):
        if (value1-value2) != 0:  
            ratios.append(round((value1 / (value1-value2)), 2))
        else:
            ratios.append('n/a')  # Handle cases where value2 is 0
    return ratios


def visualize_for_date(movie_title, opinions):
    dates = list(set(opinions[0]))
    dates = sort_and_pad_dates(dates)

    positive_values = [opinions[1][date] for date in dates]
    negative_values = [opinions[2][date] for date in dates]
    overall = [opinions[3][date] for date in dates]

    pos = sum(positive_values)
    neg = sum(negative_values)
    pos_ratio = round(pos/(pos-neg), 2)
    ratios = calculate_ratios(positive_values, negative_values)

    pn_graph = plt
    pn_graph.clf()

    pn_graph.bar(dates, positive_values, color='pink', label='positive', width=0.2)
    pn_graph.bar(dates, negative_values, color='orange', label='negative', width=0.2)
    pn_graph.scatter(dates, overall, marker="_", color='black', label='net opinion', linewidths=1.5)
    

    min_y = min(negative_values) * 1.05
    for i, value in enumerate(ratios):
        pn_graph.annotate(value, (dates[i], min_y), fontsize=5)

    pn_graph.xlabel('date')
    pn_graph.ylabel('number of opinions')
    pn_graph.title(f'{movie_title} opinions over time, positive ratio: {pos_ratio}')
    pn_graph.xticks(rotation=45)
    pn_graph.legend()

    pn_graph.tight_layout()
    return pn_graph