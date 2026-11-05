class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        for p in range(n2):
            if sorted(s1) == sorted(s2[p:p+n1]):
                return True
        return False