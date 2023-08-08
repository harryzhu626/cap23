import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime

def visualize_data(data_positive, data_negative):
    dates_positive = [datetime.strptime(date, "%Y-%m-%d") for date, _ in data_positive]
    values_positive = [value for _, value in data_positive]

    dates_negative = [datetime.strptime(date, "%Y-%m-%d") for date, _ in data_negative]
    values_negative = [value for _, value in data_negative]

    plt.figure(figsize=(10, 6))
    plt.plot(dates_positive, values_positive, marker='o', linestyle='-', color='b', label='Positive Group')
    plt.plot(dates_negative, values_negative, marker='x', linestyle='--', color='r', label='Negative Group')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Data Points Plot')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)

def main():
    st.title("Grouped Data Visualizer")

    # Input positive data points from the user
    input_data_positive = st.text_area("Enter positive data points (date, value):", "2023-08-01, 10\n2023-08-05, 15\n2023-08-10, 25")

    # Input negative data points from the user
    input_data_negative = st.text_area("Enter negative data points (date, value):", "2023-08-03, -5\n2023-08-07, -10\n2023-08-12, -8")

    data_positive = [tuple(line.split(',')) for line in input_data_positive.split('\n')]
    data_negative = [tuple(line.split(',')) for line in input_data_negative.split('\n')]

    if st.button("Visualize"):
        visualize_data(data_positive, data_negative)

if __name__ == "__main__":
    main()
