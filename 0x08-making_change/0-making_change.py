#!/usr/bin/python3
"""
Script determines the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet the total.

    Parameters:
        coins (list): List containing denominations of coins.
        total (int): The total amount.

    Return:
        (int) The number of coins that could be used
        or -1 if the total cannot be met.
    """
    sorted_list = []
    coin_divs = 0

    if total == 0:
        return 0

    # Sort coins in descending order
    while coins:
        max_element = max(coins)
        sorted_list.append(max_element)
        coins.remove(max_element)

    for coin in sorted_list:
        while total >= coin:
            total -= coin
            coin_divs += 1

    if total > 0:
        return -1

    return coin_divs
