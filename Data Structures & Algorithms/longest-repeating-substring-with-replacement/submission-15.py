class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ele_freq = defaultdict(int)
        lef = 0
        res = 0

        for rig in range(len(s)):
            ele_freq[s[rig]] += 1

            
            while (rig-lef+1) - max(ele_freq.values())>k:
                ele_freq[s[lef]] -= 1
                lef += 1
            res = max(res, rig-lef+1)
        return res 