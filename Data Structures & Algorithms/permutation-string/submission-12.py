class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        sorted_s1 = sorted(s1)
        for i in range(n2):
            if sorted(s2[i:i+n1]) == sorted_s1:
                return True
        return False