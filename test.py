import numpy as np

def log_normalize(data):
    min_val = min(data)
    normalized_data = [(np.log(x) - np.log(min_val + 1)) for x in data]  # Adding 1 to avoid log(0)
    return normalized_data

# Sample data
y_values_list1 = [-100, 50, 0, 75, 100]
y_values_list2 = [1000, -200, 0, -500, 800]

# Log-normalize the data
log_normalized_list1 = log_normalize(y_values_list1)
log_normalized_list2 = log_normalize(y_values_list2)

# Print the log-normalized lists
print("Log-Normalized List 1:", log_normalized_list1)
print("Log-Normalized List 2:", log_normalized_list2)
