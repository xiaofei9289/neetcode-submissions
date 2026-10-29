class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = [0]

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                if profit < 0:
                    profit = 0
                res.append(profit)
        return max(res)
        
        