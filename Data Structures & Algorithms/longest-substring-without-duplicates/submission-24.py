class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lef = 0
        res= 0
        store = set()
        for rig in range(len(s)):
            while s[rig] in store:
                store.remove(s[lef])
                lef += 1
            store.add(s[rig])
            res = max(res, rig-lef+1)
        return res
