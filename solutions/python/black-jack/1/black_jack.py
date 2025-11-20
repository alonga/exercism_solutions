"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""

    # If an Ace is already present in the hand → forced to take it as 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # No Ace in hand → compute total normally
    total = value_of_card(card_one) + value_of_card(card_two)

    # If adding 11 does not bust (≤ 21 total), use 11
    return 11 if total + 11 <= 21 else 1



def is_blackjack(card_one, card_two):
    values = sorted([card_one, card_two])
    return ('A' in values) and (value_of_card(values[0]) + value_of_card(values[1]) == 11)


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
