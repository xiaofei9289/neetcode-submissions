class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer=0
        longest=0
        count={}

        for right_pointer in range(len(s)):
            char=s[right_pointer]
            if char in count:
                count[char]+=1
            else:
                count[char]=1

            while (right_pointer-left_pointer+1) - max(count.values())>k:
                count[s[left_pointer]]-=1
                left_pointer+=1
            longest=max(longest,right_pointer-left_pointer+1)
        return longest