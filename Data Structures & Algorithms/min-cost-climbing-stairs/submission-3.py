class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            cost_a = dp[i-1] + cost[i-1]
            cost_b = dp[i-2] + cost[i-2]
            dp[i] = min(cost_a,cost_b)
        return dp[n]