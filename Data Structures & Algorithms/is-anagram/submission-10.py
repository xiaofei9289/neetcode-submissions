class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ele in s:
            if ele not in t:
                return False
            else:
                t=t.replace(ele,"",1)
        if len(t) == 0:
            return True
        else: 
            return False