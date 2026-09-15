class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        freq= set()
        left=0
        for right in range(len(s)):
            while s[right] in freq:
                freq.remove(s[left])
                left+=1
            freq.add(s[right])
            lenghth=right-left+1
            res=max(res, lenghth)
        return res