class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0 
        for right in range(len(s)):
            ele = s[right]
            if ele in map and map[ele]>=left:
                left = map[ele] + 1
            map[ele] = right
            res = max(right-left+1,res)
        return res