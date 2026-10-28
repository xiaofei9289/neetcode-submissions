class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0 
        res = 1
        seen = {}
        for right in range(len(s)):
            char = s[right]

            if char in seen and seen[char]>=left:
                left = seen[char] + 1

            seen[char] = right
            length = right - left + 1
            res = max(res,length)
        return res