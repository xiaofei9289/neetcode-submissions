class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)

        for ele in t:
            need[ele] += 1
        
        window = defaultdict(int)
        left = 0 
        res = ""
        min_length = float("inf")
        required = len(need)
        have = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in need and window[char]==need[char]:
                have += 1
                while have == required:
                    length = right - left + 1
                    if length < min_length:
                        min_length = length
                        res = s[left:right + 1]
                    left_char = s[left]
                    window[left_char] -= 1
                    if left_char in need and window[left_char] < need[left_char]:
                        have -= 1

                    left += 1

        return res
