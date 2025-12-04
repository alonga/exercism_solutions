from collections import Counter

RANK_ORDER = "23456789TJQKA"
RANKS = {r: i for i, r in enumerate(RANK_ORDER, start=2)}

def parse_card(card):
    # Handle both "10H" and "TH"
    if card.startswith("10"):
        return 10, card[2]
    return RANKS[card[0]], card[1]


def hand_rank(hand):
    cards = hand.split()
    ranks, suits = zip(*(parse_card(c) for c in cards))
    ranks = sorted(ranks, reverse=True)
    is_flush = len(set(suits)) == 1

    # Wheel straight: A-2-3-4-5
    is_straight = False
    if ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        straight_high = 5
    elif all(ranks[i] - 1 == ranks[i + 1] for i in range(4)):
        is_straight = True
        straight_high = ranks[0]

    cnt = Counter(ranks)
    ordered = sorted(cnt.items(), key=lambda x: (-x[1], -x[0]))
    pattern = tuple(v for _, v in ordered)
    sorted_ranks = [rank for rank, _ in ordered for _ in range(cnt[rank])]

    # Evaluate hand category
    if is_flush and is_straight:
        return (8, straight_high)
    if pattern == (4, 1):
        return (7, sorted_ranks)
    if pattern == (3, 2):
        return (6, sorted_ranks)
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, straight_high)
    if pattern == (3, 1, 1):
        return (3, sorted_ranks)
    if pattern == (2, 2, 1):
        return (2, sorted_ranks)
    if pattern == (2, 1, 1, 1):
        return (1, sorted_ranks)
    return (0, ranks)


def best_hands(hands):
    scored = [(hand_rank(h), h) for h in hands]
    best = max(scored)[0]
    return [h for score, h in scored if score == best]
