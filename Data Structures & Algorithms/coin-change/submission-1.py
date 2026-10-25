class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=amount
        dp = [float("inf")]*(n+1)
        dp[0] = 0

        for i in range(1,n+1):
            for coin in coins:
                if i>=coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[n] == float('inf'):
            return -1
        return dp[n]