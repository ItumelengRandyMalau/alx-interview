#!/usr/bin/python3
"""Making change algorithm"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    makeChange is a method that determine the fewest number
    of coins needed to meet a given amount total.

    Args:
        - coins[int]: list of indefinite coins to make change.
        - total(int): total amount given to make change for.
    Returns:
        returns fewest number of coins needed to meet total(int).
    Algorithm Used:
        Greedy algorithm.
    """

    if total <= 0:
        return 0

    amount = total
    coinCount = 0
    coinIndex = 0
    coins_len = len(coins)
    sortedCoins = sorted(coins, reverse=True)

    while amount > 0:
        if coinIndex >= coins_len:
            return -1
        if amount - sortedCoins[coinIndex] >= 0:
            amount -= sortedCoins[coinIndex]
            coinCount += 1
        else:
            coinIndex += 1
    return coinCount
