from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

amount = 6
coins = [1, 3, 4]
amount = 4
coins = [2]
solution = Solution()
print(solution.coinChange(coins, amount))
