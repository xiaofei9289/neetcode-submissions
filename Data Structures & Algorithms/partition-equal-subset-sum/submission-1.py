class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        # 总和为奇数，不可能平分
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        # 创建二维 DP 数组
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # 凑出总和 0 永远是可能的
        for i in range(n + 1):
            dp[i][0] = True

        # i 表示考虑前 i 个数字
        for i in range(1, n + 1):

            # j 表示目标总和，可以正序遍历
            for j in range(1, target + 1):

                # 当前数字
                num = nums[i - 1]

                if j >= num:

                    # 不选当前数字 OR 选择当前数字
                    dp[i][j] = (
                        dp[i - 1][j] or
                        dp[i - 1][j - num]
                    )

                else:
                    # 当前数字大于目标，只能不选
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]