class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        freq=defaultdict(int)
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            res=max(right-left+1,res)
        return res
        