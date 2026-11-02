class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        dp = [1] * n
        sorted_nums = sorted(nums)
        for i in range(1,n):
            if sorted_nums[i] == sorted_nums[i-1]:
                dp[i] = dp[i-1]
            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)