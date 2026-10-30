class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Window(t)
        left = 0 
        start = 0
        min_length = float("inf")

        for right in range(len(s)):
            window.add(s[right])
            while window.is_covered():
                cur_length = right - left + 1
                if cur_length < min_length:
                    min_length = cur_length
                    start = left
                window.remove(s[left])
                left += 1
        if min_length == float("inf"):
            return ""
        return s[start:start+min_length]




class Window:
    def __init__(self, t:str) -> None:
        self.need = Counter(t)
        self.window = Counter()
        self.valid = 0
    
    def add(self, c: str) -> None:
        if c in self.need:
            self.window[c] += 1
            if self.window[c] == self.need[c]:
                self.valid += 1
    
    def remove(self, c:str) -> None:
        if c in self.need:
            if self.window[c] == self.need[c]:
                self.valid -= 1
            self.window[c] -= 1
    
    def is_covered(self) -> bool:
        return self.valid == len(self.need)
