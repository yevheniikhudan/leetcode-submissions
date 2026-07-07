class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for num in prices:
            min_price = min(min_price, num)
            max_profit = max(max_profit, num - min_price)
        return max_profit