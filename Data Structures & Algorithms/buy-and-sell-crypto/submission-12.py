class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lef = 0
        max_profit = 0
        for rig in range(len(prices)):
            if prices[rig] < prices[lef]:
                lef = rig
            profit = prices[rig] - prices[lef]
            max_profit = max(profit, max_profit)
        return max_profit