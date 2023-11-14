import time
import random

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') # backend (https://matplotlib.org/stable/users/explain/figure/backends.html)

from knapsack import ks_brute_force, ks_rec


# Function to generate random weights and values for 'n' items
def generate_items(n, max_weight, max_value):
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
    return items

def measure_runtime(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Experiment settings
max_items = 150
max_weight = 5
max_value = 100
step = 5

# Lists to store the results
brute_force_runtimes = []
ks_rec_runtimes = []
item_counts = list(range(1, max_items + 1, step))

# Run experiments for different numbers of items
for item_count in item_counts:
    items = generate_items(item_count, max_weight, max_value)

    # Measure runtime for ks_brute_force
    brute_force_time = measure_runtime(ks_brute_force, items, max_weight)
    brute_force_runtimes.append(brute_force_time)

    # Measure runtime for ks_rec
    rec_time = measure_runtime(ks_rec, items, item_count, max_weight)
    ks_rec_runtimes.append(rec_time)

# Reference: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html

fig, ax = plt.subplots(figsize=(10, 6))  # Create a new figure and axis
ax.plot(item_counts, brute_force_runtimes, label='ks_brute_force')
ax.plot(item_counts, ks_rec_runtimes, label='ks_rec')
ax.set_xlabel('Number of Items')
ax.set_ylabel('Runtime (seconds)')
ax.set_title('Runtime of Knapsack Implementations vs Number of Items')
ax.legend()
plt.show()