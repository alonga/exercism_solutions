from functools import lru_cache
from itertools import combinations

# Base price in cents
BOOK_PRICE = 800

# Discounted price multipliers in percent (for groups of distinct books)
# size -> percent of full price
DISCOUNT_PERCENT = {
    1: 100,  # no discount
    2: 95,
    3: 90,
    4: 80,
    5: 75,
}


def total(basket):
    """
    basket: list of integers 1–5 representing the book volumes.
    Return: minimal total price in *cents* (int).
    """

    if not basket:
        return 0

    # We always have at most 5 different titles: 1, 2, 3, 4, 5
    counts = [0] * 5
    for book in basket:
        # book numbers are 1..5
        counts[book - 1] += 1

    counts = tuple(counts)  # make hashable for caching

    @lru_cache(maxsize=None)
    def dp(state):
        # state is a 5-tuple of remaining counts for each title
        if sum(state) == 0:
            return 0  # no books left => no cost

        best = float("inf")
        indices = [i for i, c in enumerate(state) if c > 0]

        # Try all possible non-empty subsets of distinct books to form a group
        for group_size in range(1, len(indices) + 1):
            for subset in combinations(indices, group_size):
                new_state = list(state)
                for idx in subset:
                    new_state[idx] -= 1

                # cost of this group in cents
                group_cost = (
                    group_size * BOOK_PRICE * DISCOUNT_PERCENT[group_size] // 100
                )

                total_cost = group_cost + dp(tuple(new_state))
                if total_cost < best:
                    best = total_cost

        return best

    return dp(counts)


