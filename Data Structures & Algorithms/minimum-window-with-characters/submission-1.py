class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s)<len(t):
            return ""
        need={}
        window={}

        for char in t:
            need[char]=need.get(char,0)+1
        left=0
        have=0
        required=len(need)

        best_start=0
        best_lengt=len(s)+1
        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char,0)+1
            
            if char in need and window[char]==need[char]:
                have+=1
            while have==required:
                current_length=right-left+1

                if current_length<best_lengt:
                    best_start=left
                    best_lengt=current_length
                char=s[left]
                window[char]-=1

                if char in need and window[char]<need[char]:
                    have-=1
                left+=1
        if best_lengt==len(s)+1:
            return ""
        return s[best_start:best_start+best_lengt]

        