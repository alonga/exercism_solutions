def find_fewest_coins(coins, target):
    # Special required message for negative target
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    coins = sorted(coins)

    dp = [None] * (target + 1)
    dp[0] = []

    for amount in range(1, target + 1):
        best = None
        for c in coins:
            if c > amount:
                break
            prev = dp[amount - c]
            if prev is not None:
                candidate = prev + [c]
                if best is None or len(candidate) < len(best):
                    best = candidate
        dp[amount] = best

    # Required message when change cannot be made
    if dp[target] is None:
        raise ValueError("can't make target with given coins")

    # Tests expect ascending sorted order
    return sorted(dp[target])

