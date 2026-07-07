class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buy)

            if buy:
                return max(dfs(i + 1, False) - prices[i], cooldown)
            else:
                return max(dfs(i + 2, True) + prices[i], cooldown)

        return dfs(0, True)
    