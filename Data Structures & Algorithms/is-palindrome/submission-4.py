class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        s1 = "".join(res)

        p1 = 0 
        p2 = len(s1)-1

        while p1<p2:
            if s1[p1]!=s1[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

        