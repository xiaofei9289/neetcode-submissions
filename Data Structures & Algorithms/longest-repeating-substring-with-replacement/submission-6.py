class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        left=0
        res=0
        for right in range(len(s)):
            freq[s[right]]+=1
            window_size=right-left+1
            most_freq_ele=max(freq.values())
            while window_size-most_freq_ele>k:
                freq[s[left]]-=1
                left+=1
                
                window_size=right-left+1
                most_freq_ele=max(freq.values())
            res=max(window_size,res)
        return res
        