class Solution:
    def isPalindrome(self, s: str) -> bool:
        dealed = ""
        for ele in s:
            if ele.isalnum():
                dealed += ele.lower()
        return dealed == dealed[::-1]
        