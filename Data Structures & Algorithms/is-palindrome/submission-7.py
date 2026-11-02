class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ele in s:
            if ele.isalnum():
                res += ele.lower()
        p1 = 0
        p2 = len(res)-1
        while p1 <= p2:
            if res[p1] == res[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True