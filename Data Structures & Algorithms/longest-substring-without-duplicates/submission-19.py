class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left_pointer = 0 
        res = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in seen:
                
                seen.remove(s[left_pointer])
                left_pointer += 1
            seen.add(s[right_pointer])
            res = max(right_pointer-left_pointer+1, res)
        return res