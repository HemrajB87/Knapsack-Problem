//Implementation 1
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
    items = [(2, 16), (10, 10), (15, 3)]
    capacity = 25
    max_value = ks_brute_force(items, capacity)
    print(f"Maximum value for given items and capacity: {max_value}")

//Implementation 2
def ks_rec(x, y):
    # Base cases
    if x == 0:
        return 0
    if y == 0:
        return 0


    if items[x - 1][0] > y:
        # cur item's weight > then available capacity
        return ks_rec(x - 1, y)
    else:
        # Returns max profit achieved by including or excluding the current item.
        return max(ks_rec(x - 1, y), ks_rec(x - 1, y - items[x - 1][0]) + items[x - 1][1])

# format: (weight, profit)
items = [(3, 10), (4, 15), (5, 30), (7, 40)] # example inorder to not make items "unresolved"

max_value = ks_rec(len(items), 10)

print("Max:", max_value)
