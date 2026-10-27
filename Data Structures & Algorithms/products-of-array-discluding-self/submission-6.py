class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lef = n * [1]
        lef[0] = 1
        for i in range(1, n):
            lef[i] = lef[i-1] * nums[i-1]
        
        rig = [1] * n
        rig[n-1] = 1
        for i in range(n-2, -1, -1):
            rig[i] = rig[i+1] * nums[i+1]
        
        res = n * [1]
        for i in range(n):
            res[i] = lef[i] * rig[i]
        return res        
