# dp_solver.py

def solve(weights, values, capacity):
    # Making the dp array
    n = len(weights)
    dp = [0 for i in range(capacity + 1)]

    # Taking first i elements
    for i in range(1, n + 1):

        # Starting from back,
        # so that we also have data of
        # previous computation when taking i-1 items
        for w in range(capacity, 0, -1):
            if weights[i - 1] <= w:
                # Finding the maximum value
                dp[w] = max(dp[w], dp[w - weights[i - 1]] + values[i - 1])

    return dp[capacity]

def solve_2d(W, wt, val):
    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]