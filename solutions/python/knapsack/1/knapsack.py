def maximum_value(maximum_weight, items):
    dp = [0] * (maximum_weight + 1)

    for item in items:
        weight = item["weight"]
        value = item["value"]

        if weight == 0:
            # Add value to all capacities, since unlimited weight use is allowed
            for w in range(maximum_weight + 1):
                dp[w] += value
        else:
            for w in range(maximum_weight, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[maximum_weight]

