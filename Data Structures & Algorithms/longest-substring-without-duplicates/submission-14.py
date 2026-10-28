class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = 1
        seen = {s[0]:0}
        for i in range(1, n):
            char = s[i]
            if char in seen:
                j = seen[char]
                dp[i] = min(dp[i-1]+1, i-j)
            else:
                dp[i] = dp[i-1]+1
            seen[char] = i
        return max(dp)