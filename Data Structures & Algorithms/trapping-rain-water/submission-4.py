class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = 0 
        right = n-1
        lef_max = height[left]
        rig_max = height[right]
        res= 0

        while left<right:
            if lef_max<rig_max:
                left += 1
                lef_max = max(lef_max,height[left])
                res = res + lef_max - height[left]
            else:
                right -= 1
                rig_max = max(rig_max,height[right])
                res = res + rig_max - height[right]
        return res