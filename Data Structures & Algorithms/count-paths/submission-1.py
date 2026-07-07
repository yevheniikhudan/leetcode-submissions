class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for _ in range(m):
            for col in range(1, n + 1):
                dp[col] = dp[col] + dp[col - 1]

        return dp[n]