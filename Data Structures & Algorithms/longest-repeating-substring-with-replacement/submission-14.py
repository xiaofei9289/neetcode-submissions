class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lef = 0
        res = 0
        map = defaultdict(int)
        window_size = 0

        for rig in range(len(s)):
            ele = s[rig]
            map[ele] += 1
            window_size = rig - lef + 1
            while window_size - max(map.values())>k:
                map[s[lef]] -= 1
                lef += 1
                window_size = rig - lef + 1
            res = max(res, window_size)

        return res 
            


