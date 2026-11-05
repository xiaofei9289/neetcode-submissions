class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for eke in prices:
            min_price = min(eke, min_price)
            profit = eke - min_price
            max_profit = max(profit,max_profit)
        return max_profit