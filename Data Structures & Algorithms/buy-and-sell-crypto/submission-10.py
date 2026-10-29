class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for ele in prices:
            min_price = min(ele, min_price)
            profit = ele - min_price
            max_profit = max(profit,max_profit)
        return max_profit
        