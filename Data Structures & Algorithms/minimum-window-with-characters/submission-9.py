class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        left = 0
        start = 0 
        min_length = float("inf")

        for right in range(len(s)):
            ele = s[right]
            window[ele] += 1

            while self.valid(need,window):
                cur_length = right- left + 1
                if cur_length < min_length:
                    min_length = cur_length
                    start = left
                
                window[s[left]] -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        return s[start:start + min_length]

    
    def valid(self, need, window):
        for ele in need:
            if window[ele]<need[ele]:
                return False
        return True