#!/usr/bin/python3
""" makeChange module
"""


def makeChange(coins, total):
    """
    This function finds the fewest number of coins needed to make a certain amount.

    Args:
      coins: A list of coin values (integers greater than 0).
      total: The total amount to reach (integer).

    Returns:
      The fewest number of coins needed to make the total, or -1 if it's impossible.
    """
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin

    if total != 0:
        return -1
    
    return count
