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