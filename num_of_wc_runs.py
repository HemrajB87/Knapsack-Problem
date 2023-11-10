#used to undertsand approach: https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
def num_of_wc_runs(n, m):

    #stores solutions to subproblems
    bottom_up = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases
    if m == 0:
        return 0

    for i in range(1, n + 1):
        bottom_up[i][1] = i - 1

    for j in range(2, m + 1):
        bottom_up[1][j] = 0
        bottom_up[2][j] = 1

    # Bottom-up dynamic programming
    for j in range(2, m + 1):
        for i in range(3, n + 1):
            bottom_up[i][j] = float('inf')
            for k in range(1, i + 1):
                bottom_up[i][j] = min(bottom_up[i][j], 1 + max(bottom_up[k-1][j-1], bottom_up[i-k][j]))

    return bottom_up[n][m]

# example for function operation
n = 105
m = 1
result = num_of_wc_runs(n, m)
print(f"Number of worst-case runs for {m} bricks and {n} force settings: {result}")