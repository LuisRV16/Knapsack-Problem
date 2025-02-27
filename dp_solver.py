def solve(weights, values, capacity):
    n = len(weights)
    # Create a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table.
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find which items to include.
    solution = [0] * n
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            solution[i - 1] = 1
            w -= weights[i - 1]
        # else: solution[i-1] remains 0

    return solution