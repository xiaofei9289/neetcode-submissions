class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lef_max = [0] * n
        lef_max[0] = height[0]
        for i in range(1,n):
            lef_max[i] = max(lef_max[i-1],height[i])
        rig_max = [0] * n 
        rig_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rig_max[i] = max(rig_max[i+1],height[i])

        res= 0

        for i in range(n):
            sum = min(lef_max[i],rig_max[i]) - height[i]
            res = res + sum
        return res
        
