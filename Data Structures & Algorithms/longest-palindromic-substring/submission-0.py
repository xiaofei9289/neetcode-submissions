class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [False] * n

        start = 0
        max_length = 0
        for i in range(n-1,-1,-1):
            for j in range(n - 1, i - 1, -1):
                length = j - i + 1
                if s[i] == s[j]:
                    if length <= 3:
                        dp[j] = True

                    else:
                        dp[j] = dp[j - 1]
                else:
                    dp[j] = False
                if dp[j] and length > max_length:
                    max_length = length
                    start = i

        return s[start:start + max_length]