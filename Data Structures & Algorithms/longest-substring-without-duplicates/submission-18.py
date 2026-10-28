class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        left = 0
        res = 0

        for right in range(len(s)):
            char = s[right]
            if char in store and store[char] >= left:
                left = store[char]+1
            store[char] = right
            res = max(res, right-left+1)
        return res