class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        dp = []
        for i in range(n+1):
            row = [False] * (target+1)
            dp.append(row)
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1,target+1):
                num = nums[i - 1]
                if j >= num:
                    dp[i][j] = (
                        dp[i - 1][j] or
                        dp[i - 1][j - num]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]
        