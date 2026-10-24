class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_array = [0] * (len(cost)+1)
        dp_array[0] = 0
        dp_array[1] = 0

        for i in range(2,len(cost)+1):
            dp_array[i] = min(dp_array[i-1]+cost[i-1],dp_array[i-2]+cost[i-2])
        
        return dp_array[len(cost)]