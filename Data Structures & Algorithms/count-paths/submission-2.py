class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            row = [0] * n
            dp.append(row)
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for a in range(1,m):
            for b in range(1,n):
                dp[a][b] = dp[a-1][b] + dp[a][b-1]
        return dp[m-1][n-1]