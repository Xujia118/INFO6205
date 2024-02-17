from typing import List

class Solution:
    def __init__(self, amount, coins) -> None:
        self.amount = amount
        self.coins = coins

    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = self._coinChange(coins, amount, {})
        return ans if ans != float('inf') else -1

    def _coinChange(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount < 0:
            return float('inf')

        if amount == 0:
            return 0

        min_coins = float('inf')
        for coin in coins:
            cur_coins = self._coinChange(coins, amount - coin, memo) + 1

            if cur_coins < min_coins:
                min_coins = cur_coins

        memo[amount] = min_coins
        return min_coins
