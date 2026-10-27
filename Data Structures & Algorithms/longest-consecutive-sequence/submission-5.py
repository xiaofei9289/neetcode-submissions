class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0 
        nums.sort()

        dp = [1] * n
        dp[0] = 1
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            elif nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = 1
        return max(dp)