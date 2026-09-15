class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        lef=0
        freq=defaultdict(int)
        for right in range(len(s)):
            freq[s[right]]+=1
            while freq[s[right]]>1:
                freq[s[lef]]-=1
                lef+=1
            res=max(right-lef+1,res)
        return res
        