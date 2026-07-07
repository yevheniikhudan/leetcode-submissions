class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(1, len(dp)):
                remainder = a - coin
                if remainder >= 0:
                    dp[a] = min(dp[a], 1 + dp[remainder])

        return -1 if dp[amount] == float("inf") else dp[amount]