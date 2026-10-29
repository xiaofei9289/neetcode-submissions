class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        lef = 0
        max_length = 1
        max_freq = 1
        map = defaultdict(int)

        for rig in range(n):
            ele = s[rig]
            map[ele] += 1 
            max_freq = max(max_freq,map[ele])
            while (rig-lef+1) - max_freq > k:
                map[s[lef]] -= 1
                lef += 1
            max_length = max(max_length, rig-lef+1)
        return max_length
            