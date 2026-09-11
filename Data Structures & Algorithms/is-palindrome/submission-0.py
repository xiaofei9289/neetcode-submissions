class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_pointer=0
        end_pointer=len(s)-1
        while start_pointer<end_pointer:
            if not s[start_pointer].isalnum():
                start_pointer += 1
                continue

            if not s[end_pointer].isalnum():
                end_pointer -= 1
                continue
            if s[start_pointer].lower()!=s[end_pointer].lower():
                return False
            start_pointer+=1
            end_pointer-=1
        return True
        