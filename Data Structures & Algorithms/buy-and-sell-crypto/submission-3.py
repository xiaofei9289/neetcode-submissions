class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = [0]
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                num = prices[j] - prices[i]
                res.append(num)
        return max(res)