class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        lef = 0 
        freq = defaultdict(int)
        for rig in range(len(s)):
            freq[s[rig]] += 1
            while (rig-lef+1) - max(freq.values())>k:
                freq[s[lef]] -= 1
                lef += 1
            res = max(rig-lef +1 ,res)
        return res