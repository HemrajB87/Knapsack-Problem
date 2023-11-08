# 1. Imports
import time
from random import randint
import matplotlib.pyplot as plt
from knapsack import ks_bottom_up, ks_top_down

# Helper function to measure the runtime of a function
def measure_runtime(func, items, capacity):
    start_time = time.time()
    func(items, capacity)
    end_time = time.time()
    return end_time - start_time

# Experiment function to run the knapsack algorithm and collect runtime data
def knapsack_runtime_experiment(func, item_counts, max_capacity,  min_value, max_value, min_weight, max_weight, iterations):
    results = {}
    for count in item_counts:
        average_runtime = 0
        for _ in range(iterations):
            items = [(randint(min_value, max_value), randint(min_weight, max_weight)) for _ in range(count)]
            runtime = measure_runtime(func, items, max_capacity)
            average_runtime += runtime
        average_runtime /= iterations
        results[count] = average_runtime
    return item_counts, [results[count] for count in item_counts]



# Bottom up is better: Large number of items with small weights and high values
def plot1_results():
    item_counts = range(10, 501, 10)  # Varying number of items
    max_capacity = 50  # Maximum capacity of the knapsack
    iterations = 100  # Number of iterations to average out the runtime
    min_weight = 1
    max_weight = 5
    min_value = 50
    max_value = 100

    plt.figure(figsize=(10, 6))

    # Running experiments for both bottom-up and top-down approaches

    x, y = knapsack_runtime_experiment(ks_bottom_up, item_counts, max_capacity,  min_value, max_value, min_weight, max_weight, iterations)
    plt.plot(x, y, label='Bottom-Up')
    x, y = knapsack_runtime_experiment(ks_top_down, item_counts, max_capacity,  min_value, max_value, min_weight, max_weight, iterations)
    plt.plot(x, y, label='Top-Down')

    plt.title('Knapsack Algorithm Runtime Comparison (BU is better)')
    plt.xlabel('Number of Items')
    plt.ylabel('Average Runtime (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

# Run the experiment and generate the plot
#plot1_results()


#Top-down is better: Small number of items with weights close to the knapsack's capacity and a smaller value:weight ratio (much more specific because BU is usually better)
def plot2_results():
    item_counts = range(10, 501, 5)  
    max_capacity = 50 
    iterations = 100  
    min_weight = 25
    max_weight = 50
    min_value = 1
    max_value = 10

    plt.figure(figsize=(10, 6))

    x, y = knapsack_runtime_experiment(ks_bottom_up, item_counts, max_capacity,  min_value, max_value, min_weight, max_weight, iterations)
    plt.plot(x, y, label='Bottom-Up')
    x, y = knapsack_runtime_experiment(ks_top_down, item_counts, max_capacity,  min_value, max_value, min_weight, max_weight, iterations)
    plt.plot(x, y, label='Top-Down')


    plt.title('Knapsack Algorithm Runtime Comparison (TD is better)')
    plt.xlabel('Number of Items')
    plt.ylabel('Average Runtime (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

# Run the experiment and generate the plot
plot2_results()
