from collections import defaultdict
import matplotlib.pyplot as plt
from helper.datetrimmer import date_trimmer
import streamlit as st 

positive_counts = defaultdict(int)
negative_counts = defaultdict(int)


def congregate_data(opinions):
    for opinion, date in opinions:
        date = date_trimmer(date)
        if opinion == 'POSITIVE':
            positive_counts[date] += 1
        elif opinion == 'NEGATIVE':
            negative_counts[date] -= 1
        yield date, opinion


def visualize_for_date(opinions):
    dates = [date for date, _ in opinions]

    positive_values = [positive_counts[date] for date in dates]
    negative_values = [negative_counts[date] for date in dates]

    plt.bar(dates, positive_values, color='blue', label='positive')
    plt.bar(dates, negative_values, color='red', label='negative')

    plt.xlabel('Date')
    plt.ylabel('Number of Opinions')
    plt.title('Opinions Over Time')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    # plt.show()
    st.pyplot(plt)