class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        target =sorted(s1)

        for i in range(len(s2)-n+1):
            window = s2[i:i+n]
            if sorted(window) == target:
                return True
        return False

