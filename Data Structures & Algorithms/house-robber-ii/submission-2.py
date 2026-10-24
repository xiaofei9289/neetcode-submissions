class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        
        case1 = self.helper(nums[:-1])
        case2 = self.helper(nums[1:])

        return max(case1, case2)


    
    def helper(self, nums:List[int])->int:
        n = len(nums)

        if n == 0:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(
                dp[i - 1],
                dp[i - 2] + nums[i - 1]
            )

        return dp[n]