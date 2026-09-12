class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer_left=0
        seen=set()
        res=0
        for pointer_right in range(len(s)):
            while s[pointer_right] in seen:
                seen.remove(s[pointer_left])
                pointer_left+=1
            seen.add(s[pointer_right])
            res=max(res,pointer_right-pointer_left+1)
        return res

