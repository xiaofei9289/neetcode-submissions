class Solution:
    def isPalindrome(self, s: str) -> bool:
        dealed = "".join(ele.lower() for ele in s if ele.isalnum())
        return dealed == dealed[::-1]