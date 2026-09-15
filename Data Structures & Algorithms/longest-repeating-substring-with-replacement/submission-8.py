class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        left=0
        freq=defaultdict(int)
        for right in range(len(s)):
            freq[s[right]]+=1
            while (right-left+1) -max(freq.values())>k:
                freq[s[left]]-=1
                left+=1
            res=max(right-left+1,res)
        return res

        