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
  # Initialize a table to store minimum coins needed for each amount up to total
  dp = [float('inf')] * (total + 1)

  # Base case: 0 amount needs 0 coins
  dp[0] = 0

  # Iterate through each amount from 1 to total
  for amount in range(1, total + 1):
    # Iterate through each coin denomination
    for coin in coins:
      # If the coin value is less than or equal to the current amount
      if coin <= amount:
        # Update the minimum coins needed for the current amount
        # if using the current coin + minimum for remaining amount is less
        dp[amount] = min(dp[amount], 1 + dp[amount - coin])

  # Return the minimum coins needed for the total amount
  # If it's still infinity, no combination of coins can make the total
  return dp[total] if dp[total] != float('inf') else -1