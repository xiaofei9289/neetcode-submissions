class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        lef = 0 
        res = 0

        for rig in range(len(s)):
            ele = s[rig]
            if ele in store and store[ele]>= lef:
                lef = store[ele] + 1
            store[ele] = rig
            res = max(res, rig-lef +1)
        return res