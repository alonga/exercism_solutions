from collections import deque
from math import gcd


def measure(bucket_one, bucket_two, goal, start_bucket):
    # Basic sanity checks / impossible situations
    if goal <= 0:
        raise ValueError("goal must be positive")

    if goal > max(bucket_one, bucket_two):
        # Can't ever hold that much water
        raise ValueError("goal larger than both buckets")

    if goal % gcd(bucket_one, bucket_two) != 0:
        # Classic water-pouring impossibility condition
        raise ValueError("goal not reachable with given buckets")

    c1, c2 = bucket_one, bucket_two

    # Determine starting state and illegal state
    if start_bucket == "one":
        initial = (c1, 0)        # fill bucket one first
        illegal = (0, c2)        # (start empty, other full) is illegal
    elif start_bucket == "two":
        initial = (0, c2)        # fill bucket two first
        illegal = (c1, 0)
    else:
        raise ValueError("start_bucket must be 'one' or 'two'")

    # Check if we succeed immediately after the first fill
    v1, v2 = initial
    if v1 == goal or v2 == goal:
        if v1 == goal:
            return (1, "one", v2)
        else:
            return (1, "two", v1)

    # BFS over all reachable states (v1, v2)
    queue = deque()
    queue.append((v1, v2, 1))  # (vol1, vol2, moves_so_far)
    visited = set()
    visited.add((v1, v2))

    while queue:
        v1, v2, moves = queue.popleft()

        candidates = []

        # 1) Fill operations
        if v1 != c1:
            candidates.append((c1, v2))     # fill bucket one
        if v2 != c2:
            candidates.append((v1, c2))     # fill bucket two

        # 2) Empty operations
        if v1 != 0:
            candidates.append((0, v2))      # empty bucket one
        if v2 != 0:
            candidates.append((v1, 0))      # empty bucket two

        # 3) Pour one -> two
        if v1 != 0 and v2 != c2:
            amt = min(v1, c2 - v2)
            candidates.append((v1 - amt, v2 + amt))

        # 4) Pour two -> one
        if v2 != 0 and v1 != c1:
            amt = min(v2, c1 - v1)
            candidates.append((v1 + amt, v2 - amt))

        for nv1, nv2 in candidates:
            # Enforce the special rule:
            # "After an action, you may not arrive at a state where the
            #  initial starting bucket is empty and the other bucket is full."
            if (nv1, nv2) == illegal:
                continue

            if (nv1, nv2) in visited:
                continue

            nmoves = moves + 1

            # Check for success
            if nv1 == goal or nv2 == goal:
                if nv1 == goal:
                    goal_bucket = "one"
                    other_amount = nv2
                else:
                    goal_bucket = "two"
                    other_amount = nv1
                return (nmoves, goal_bucket, other_amount)

            visited.add((nv1, nv2))
            queue.append((nv1, nv2, nmoves))

    # If we exhaust all states without finding the goal
    raise ValueError("impossible to get to goal")
