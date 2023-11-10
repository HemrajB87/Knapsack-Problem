#Implementation 1
from typing import List, Tuple

def ks_brute_force(items: List[Tuple[int]], capacity: int) -> int:
    def knapsack_helper(index, current_capacity):
        if index < 0:
            return 0

        weight, value = items[index]

        # If the current item's weight exceeds the remaining capacity, skip it
        if weight > current_capacity:
            return knapsack_helper(index - 1, current_capacity)

        # Consider two cases: including the current item or excluding it
        include_current = value + knapsack_helper(index - 1, current_capacity - weight)
        exclude_current = knapsack_helper(index - 1, current_capacity)

        # Return the maximum value of the two cases
        return max(include_current, exclude_current)

    # Start the recursive function with the last item and the given capacity
    return knapsack_helper(len(items) - 1, capacity)

# add more functions (ks_rec, ks_bottom_up, ks_top_down) here.

if __name__ == "__main__":
    # Example usage of ks_brute_force
    items = [(3, 10), (4, 15), (5, 30), (7, 40)]
    capacity = 10
    max_value = ks_brute_force(items, capacity)
    print(f"Maximum value for given items and capacity: {max_value}")

#Implementation 2
def ks_rec(items, x, y):
    # Base cases
    if x == 0 or y == 0:
        return 0

    if items[x - 1][0] > y:
        # Weight is more than the available capacity
        return ks_rec(items, x - 1, y)
    else:
        # Return the max of two cases: including or excluding the current item
        return max(
            ks_rec(items, x - 1, y),
            ks_rec(items, x - 1, y - items[x - 1][0]) + items[x - 1][1]
        )

# example for function operation
# format: (weight, profit)
items = [(3, 10), (4, 15), (5, 30), (7, 40)]
max_value = ks_rec(items, len(items), 10)
print("Maximum value:", max_value)


# Bottom-up
def ks_bottom_up(items, capacity):

    n = len(items)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    #print(dp)
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i-1][0] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][0]] + items[i-1][1])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][capacity]


# Top-Down
def ks_top_down(items, capacity):

    n = len(items)
    memo = [[-1 for x in range(capacity + 1)] for x in range(n + 1)]
    #print(memo)

    def ks_td_recursive(current_item, remaining_capacity):

        if current_item == 0 or remaining_capacity == 0:
            return 0
        # If the value is already calculated, return it.
        if memo[current_item][remaining_capacity] != -1:
            return memo[current_item][remaining_capacity]
        # otherwise process it 
        if items[current_item-1][0] > remaining_capacity:
            memo[current_item][remaining_capacity] = ks_td_recursive(current_item-1, remaining_capacity)

        else:
            include = items[current_item-1][1] + ks_td_recursive(current_item-1, remaining_capacity - items[current_item-1][0])
            exclude = ks_td_recursive(current_item-1, remaining_capacity)
            memo[current_item][remaining_capacity] = max(include, exclude)

        return memo[current_item][remaining_capacity]
    
    return ks_td_recursive(n, capacity)
