class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = start = 0
        min_leng = float("inf")

        for righ in range(len(s)):
            char = s[righ]
            if need[char]>0:
                missing -= 1
            need[char] -= 1
            while missing == 0:
                window_length = righ -left + 1
                if window_length < min_leng:
                    min_leng = window_length
                    start = left
                
                left_char = s[left]
                need[left_char] += 1

                if need[left_char] > 0:
                        missing += 1
                left += 1

        if min_leng == float("inf"):
            return ""

        return s[start:start + min_leng]

