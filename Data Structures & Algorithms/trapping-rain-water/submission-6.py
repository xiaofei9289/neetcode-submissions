class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        dp_lef = [0] * n
        dp_lef[0] = height[0]
        dp_rig = [0] * n
        dp_rig[n-1] = height[n-1]
        for i in range(1, n):
            dp_lef[i] = max(dp_lef[i-1],height[i])
        for i in range(n-2,-1,-1):
            dp_rig[i] =max(dp_rig[i+1],height[i])
        
        res = 0
        for i in range(n):
            res = res + min(dp_lef[i],dp_rig[i]) - height[i]
        return res