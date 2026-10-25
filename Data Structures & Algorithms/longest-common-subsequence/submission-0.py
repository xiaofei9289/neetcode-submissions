class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # 创建二维 DP 数组
        dp = []
        for i in range(m + 1):
            row = (n + 1) * [0]
            dp.append(row)

        # 遍历两个字符串
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[m][n]