class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        left=0
        res=0
        for right in range(len(s)):
            char=s[right]
            if char in count:
                count[char]+=1
            else:
                count[char]=1
            
            window_length=right-left+1
            most_freq_ele=max(count.values())
            needed_actions=window_length-most_freq_ele
            while needed_actions>k:
                count[s[left]]-=1
                left+=1

                window_length=right-left+1
                most_freq_ele=max(count.values())
                needed_actions=window_length-most_freq_ele
            res=max(window_length,res)
        return res

        