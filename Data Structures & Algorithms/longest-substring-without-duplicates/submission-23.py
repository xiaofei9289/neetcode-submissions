class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        store = set()
        res = 0
        left = 0

        for right in range(n):
            while s[right] in store:
                store.remove(s[left])
                left += 1

            store.add(s[right])
            res = max((right - left +1),res)   
        return res